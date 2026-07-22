# Coding Assessment (45 Minutes)

**Time:** 45 minutes
**Open book:** Yes — you may use your notes.
**Goal:** Use **LangChain** to call a model, build a small prompt chain, and let
an agent use one tool.

---

## Setup (before the clock starts — 5 min, not graded)

1. Make sure you have a `.env` file with your key:
   ```
   OPENROUTER_API_KEY=your_key_here
   ```
2. Make sure these packages are installed:
   ```
   pip install langchain langchain-openai python-dotenv
   ```
3. Create a new file called `my_assessment.py`.

Starting boilerplate (copy this to the top of your file):

```python
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")

model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)
```

---

## Tasks (45 minutes, 100 points total)

You only need to finish Task 1, 2, and 3 to pass. Task 4 is a small bonus.

### Task 1 — Call the model with LangChain messages (30 points)

Ask the model **one** question and print the answer.

- Import the message classes:
  `from langchain.messages import SystemMessage, HumanMessage`
- Call `model.invoke([...])` with:
  - a `SystemMessage("You are a friendly banking assistant. Answer in one short sentence.")`
  - a `HumanMessage("What is a floating interest rate?")`
- Print the reply using `response.content`.

Expected output looks something like:
```
Bot: A floating interest rate is one that can go up or down over time with the market.
```

---

### Task 2 — Build a prompt template + chain (25 points)

Instead of typing the whole question, build a **prompt template** with a
`{placeholder}` and connect it to the model with the pipe (`|`) operator.

- Import:
  ```python
  from langchain_core.prompts import ChatPromptTemplate
  from langchain_core.output_parsers import StrOutputParser
  ```
- Make a template:
  ```python
  prompt = ChatPromptTemplate.from_messages([
      ("system", "You are Meridian Bank's assistant. Answer in one sentence."),
      ("user", "Explain '{term}' to a first-time customer."),
  ])
  ```
- Compose the chain: `chain = prompt | model | StrOutputParser()`
- Run it twice with two different terms, e.g. `"EMI"` and `"CIBIL score"`,
  using `chain.invoke({"term": "EMI"})`. Print both answers.

Expected output looks something like:
```
EMI -> An EMI is a fixed monthly payment you make to repay a loan over time.
CIBIL score -> A CIBIL score is a number that shows how reliably you repay borrowed money.
```

---

### Task 3 — Give the agent one tool (25 points)

Turn a plain Python function into a **tool** and let an **agent** decide when to
call it.

- Import:
  ```python
  from langchain.agents import create_agent
  from langchain.tools import tool
  ```
- Add the `@tool` decorator above this function:
  ```python
  @tool
  def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:
      """Calculate the monthly EMI for a loan."""
      r = annual_rate / 100 / 12
      n = years * 12
      emi = principal / n if r == 0 else principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
      return {"emi": round(emi, 2)}
  ```
- Build the agent:
  ```python
  agent = create_agent(
      model,
      tools=[calculate_emi],
      system_prompt="You are Meridian Bank's assistant. Use tools for EMI maths.",
  )
  ```
- Ask it a question and print the final answer:
  ```python
  result = agent.invoke({"messages": [
      {"role": "user", "content": "What's the EMI on a 50 lakh loan at 8.4% over 25 years?"}
  ]})
  print(result["messages"][-1].content)
  ```

In a comment at the bottom of your file, write one sentence:
*"Who decided that the tool should be called — you or the agent?"*

---

### Task 4 — BONUS: make one embedding (up to +10 bonus points)

Turn a piece of text into a vector and print how long that vector is.

```python
from langchain_openai import OpenAIEmbeddings
from pydantic import SecretStr

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.environ["OPENROUTER_API_KEY"]),
    check_embedding_ctx_length=False,
)
vec = embeddings.embed_query("home loan eligibility")
print("vector length:", len(vec))
```

In a comment, write one sentence: *"What is an embedding, in your own words?"*

---

## How you will be graded

| Item | Points |
|------|--------|
| Task 1 — model call with `SystemMessage`/`HumanMessage` prints a reply | 30 |
| Task 2 — prompt template + `\|` chain runs for two terms | 25 |
| Task 3 — agent calls the EMI tool and prints the final answer + 1-sentence note | 25 |
| Code runs without errors | 20 |
| Task 4 bonus | +10 |

**Passing score: 60 / 100.**

## Submission

Save `my_assessment.py` and submit the file. Also paste a screenshot or copy
of your terminal output showing the program ran.

## Rules

- You may use your notes.
- You may **not** ask another person to write it for you.
- Small typos are fine as long as the program runs and prints the right things.
