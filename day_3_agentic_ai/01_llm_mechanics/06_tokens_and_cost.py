import os
import requests
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# MODEL = "meta-llama/llama-3.1-8b-instruct"  # The model to use for the API call
MODEL = "openai/gpt-4o-mini"  # The model to use for the API call
# MODEL = "openai/gpt-oss-120b"  # The model to use for the API call

# 1. Today's price for our model in USD and INR
catalogue = requests.get("https://openrouter.ai/api/v1/models", timeout=10).json()["data"]
pricing = next((m["pricing"] for m in catalogue if m["id"] == MODEL), None)
if pricing is None:
    raise SystemExit(f"Model {MODEL} not found in catalogue")
USD_PER_M_IN = float(pricing["prompt"]) * 1_000_000
USD_PER_M_OUT = float(pricing["completion"]) * 1_000_000
USD_INR = requests.get("https://api.frankfurter.app/latest?from=USD&to=INR", timeout=10).json()["rates"]["INR"]
print(f"{MODEL} ${USD_PER_M_IN:.2f}/M in, ${USD_PER_M_OUT:.2f}/M out, INR {USD_INR:.2f}/USD")

def price(in_tok: int, out_tok: int) -> str:
    usd = in_tok / 1_000_000 * USD_PER_M_IN + out_tok / 1_000_000 * USD_PER_M_OUT
    return f"${usd:.4f} (INR {usd * USD_INR:.4f})"

POLICY = ("meridian retail Bank offers home loans to salary and self-employed applicants aged 21 to 65."
          "salary applicants need a minimum monthly income of 25,000 the applicants total EMI is including"
          "the proposed loan must not exceed 50 percentage of net monthly income. A minimum civil score of 700 is"
          "required for standard pricing.")

prompt = f"summarize this home loan policy in three bullet points\n\n{POLICY}"

# 2. Estimate, before spending anything.
est_in = len(tiktoken.get_encoding("cl100k_base").encode(prompt))
est_out = 150  # we expect a short summary
print(f"Estimated tokens: {est_in} in, {est_out} out (guess) ->, {price(est_in, est_out)}")

# 3. Actually call the model and get the real usage
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPENROUTER_API_KEY"))
response = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=0.0)
print("=== The Model's Summary ===")
print(response.choices[0].message.content)

# 4. VERIFY: what it really cost us in tokens and money
usage = response.usage
if usage:
    print(f"Actual tokens: {usage.prompt_tokens} in, {usage.completion_tokens} out -> {price(usage.prompt_tokens, usage.completion_tokens)}")
    monthly = (usage.prompt_tokens / 1_000_000 * USD_PER_M_IN + usage.completion_tokens / 1_000_000 * USD_PER_M_OUT) * 10_000 * 30
    print(f"Estimated monthly cost for 10,000 requests/day: ${monthly:.2f} (INR {monthly * USD_INR:.2f})")