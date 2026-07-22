import os  # lets us read settings from the computer, like secret keys
import requests  # brings in a tool for fetching information from websites
import tiktoken  # brings in a tool that counts the word-pieces in text
from openai import OpenAI  # brings in the tool that talks to the AI service
from dotenv import load_dotenv  # brings in a helper that reads a hidden settings file

# Load environment variables from .env file
load_dotenv()  # reads the hidden settings file so the secret key becomes available
# MODEL = "meta-llama/llama-3.1-8b-instruct"  # The model to use for the API call
MODEL = "openai/gpt-4o-mini"  # The model to use for the API call
# MODEL = "openai/gpt-oss-120b"  # The model to use for the API call

# 1. Today's price for our model in USD and INR
catalogue = requests.get("https://openrouter.ai/api/v1/models", timeout=10).json()["data"]  # downloads the full list of AI models and their prices
pricing = next((m["pricing"] for m in catalogue if m["id"] == MODEL), None)  # finds the price info for the one model we picked
if pricing is None:  # checks whether our model was not in the list
    raise SystemExit(f"Model {MODEL} not found in catalogue")  # stops the program with an error message
USD_PER_M_IN = float(pricing["prompt"]) * 1_000_000  # works out the dollar cost for a million word-pieces of input
USD_PER_M_OUT = float(pricing["completion"]) * 1_000_000  # works out the dollar cost for a million word-pieces of output
USD_INR = requests.get("https://api.frankfurter.app/latest?from=USD&to=INR", timeout=10).json()["rates"]["INR"]  # looks up how many rupees one dollar is worth today
print(f"{MODEL} ${USD_PER_M_IN:.2f}/M in, ${USD_PER_M_OUT:.2f}/M out, INR {USD_INR:.2f}/USD")  # shows the model name and its prices

def price(in_tok: int, out_tok: int) -> str:  # makes a reusable recipe that turns word-piece counts into a money amount
    usd = in_tok / 1_000_000 * USD_PER_M_IN + out_tok / 1_000_000 * USD_PER_M_OUT  # adds up the input cost and the output cost in dollars
    return f"${usd:.4f} (INR {usd * USD_INR:.4f})"  # hands back the cost written in both dollars and rupees

POLICY = ("meridian retail Bank offers home loans to salary and self-employed applicants aged 21 to 65."  # stores a block of policy text in a box called POLICY
          "salary applicants need a minimum monthly income of 25,000 the applicants total EMI is including"
          "the proposed loan must not exceed 50 percentage of net monthly income. A minimum civil score of 700 is"
          "required for standard pricing.")

prompt = f"summarize this home loan policy in three bullet points\n\n{POLICY}"  # builds the full question by adding the policy text after the instruction

# 2. Estimate, before spending anything.
est_in = len(tiktoken.get_encoding("cl100k_base").encode(prompt))  # counts how many word-pieces our question is made of
est_out = 150  # we expect a short summary
print(f"Estimated tokens: {est_in} in, {est_out} out (guess) ->, {price(est_in, est_out)}")  # shows the guessed word-piece counts and the guessed cost

# 3. Actually call the model and get the real usage
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.environ.get("OPENROUTER_API_KEY"))  # sets up the connection to the AI service
response = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=0.0)  # sends the question to the AI and waits for its reply
print("=== The Model's Summary ===")  # prints a heading for the answer
print(response.choices[0].message.content)  # shows the AI's summary on the screen

# 4. VERIFY: what it really cost us in tokens and money
usage = response.usage  # grabs the real info about how much work the AI did
if usage:  # checks whether that usage info exists
    print(f"Actual tokens: {usage.prompt_tokens} in, {usage.completion_tokens} out -> {price(usage.prompt_tokens, usage.completion_tokens)}")  # shows the true word-piece counts and true cost
    monthly = (usage.prompt_tokens / 1_000_000 * USD_PER_M_IN + usage.completion_tokens / 1_000_000 * USD_PER_M_OUT) * 10_000 * 30  # works out the cost if we did this 10,000 times a day for a month
    print(f"Estimated monthly cost for 10,000 requests/day: ${monthly:.2f} (INR {monthly * USD_INR:.2f})")  # shows that estimated monthly cost in dollars and rupees