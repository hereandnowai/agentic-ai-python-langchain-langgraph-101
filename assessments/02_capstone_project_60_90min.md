# Capstone Project (60–90 Minutes)

**Type:** Individual submission
**Time:** 60–90 minutes

## The idea

Build a **"Meridian Bank Assistant"** using **LangChain**. It answers a
customer's banking question, and it can do **one** helper calculation (the loan
EMI) by giving the model a tool through an agent. No web app is required (a
Gradio screen is an optional bonus). No database.

You will combine two things you have practised: a prompt-template chain, and an
agent that calls a tool.

---

## What to build (step by step)

Create one file: `capstone_bank_assistant.py`.

### Part A — A prompt-template chain (REQUIRED)

1. Start from this boilerplate:
   ```python
   import os
   from langchain.chat_models import init_chat_model
   from langchain_core.prompts import ChatPromptTemplate
   from langchain_core.output_parsers import StrOutputParser
   from dotenv import load_dotenv

   load_dotenv()
   MODEL = os.environ.get("MODEL", "openai/gpt-4o-mini")
   model = init_chat_model(MODEL, model_provider="openrouter", temperature=0)
   ```
2. Build a `ChatPromptTemplate` with a `{question}` placeholder and a system
   message such as: `"You are Meridian Bank's assistant. Answer in one or two
   short sentences."`
3. Compose a chain with the pipe operator:
   `chain = prompt | model | StrOutputParser()`
4. Ask at least two general banking questions with
   `chain.invoke({"question": "..."})` and print the answers.

*(This is Part A of the grade. If you only finish Part A, you can still pass.)*

### Part B — Add the EMI tool through an agent (REQUIRED)

1. Define a `@tool`-decorated function:
   ```python
   from langchain.agents import create_agent
   from langchain.tools import tool

   @tool
   def calculate_emi(principal: float, annual_rate: float, years: int) -> dict:
       """Calculate the monthly EMI for a loan."""
       r = annual_rate / 100 / 12
       n = years * 12
       emi = principal / n if r == 0 else principal * r * (1 + r) ** n / ((1 + r) ** n - 1)
       return {"emi": round(emi, 2)}
   ```
2. Build an agent:
   ```python
   agent = create_agent(
       model,
       tools=[calculate_emi],
       system_prompt="You are Meridian Bank's assistant. Use tools for EMI maths.",
   )
   ```
3. Ask it an EMI question with
   `agent.invoke({"messages": [{"role": "user", "content": "..."}]})` and print
   `result["messages"][-1].content`.

So if the user asks *"What is the EMI on a 50 lakh loan at 8.4% for 25 years?"*,
the agent should call your tool and reply with the monthly payment.

### Part C — One small personal touch (REQUIRED, pick ONE)

Choose **any one** of these add-ons:

- **Structured output:** use `model.with_structured_output(...)` with a small
  Pydantic model (e.g. `intent`, `product`, `amount`) to pull the details out of
  a message like *"I'd like a home loan of about 30 lakh."*
- **Second tool:** add a `check_affordability(monthly_income, emi)` tool and pass
  both tools to the agent.
- **Embedding search:** put a few `Document`s into a `Chroma` store and run one
  `similarity_search(...)` to find the closest one.
- **Gradio screen:** wrap your agent in a `gr.ChatInterface`.

---

## Example run (what "done" looks like)

```
=== Meridian Bank Assistant ===

Q: What documents do I need for a home loan?
A: Usually a photo ID, PAN, address proof, salary slips, and bank statements.

Q: What is the EMI on a 50 lakh loan at 8.4% for 25 years?
(agent called calculate_emi with {'principal': 5000000, 'annual_rate': 8.4, 'years': 25})
A: Your monthly EMI is about ₹40,096.
```

Your numbers and wording can differ — that's fine.

---

## What to submit

Submit **three** things:

1. **`capstone_bank_assistant.py`** — your code.
2. **A screenshot or text copy of one full run** (a couple of questions,
   including the EMI question working through the agent).
3. **A short README (5–8 sentences)** answering:
   - What does your program do?
   - How does the agent decide when to use the EMI tool?
   - Which "personal touch" (Part C) did you pick?
   - One thing that was confusing and how you solved it.

---

## Grading (100 points)

| Part | What we check                                                          | Points |
| ---- | --------------------------------------------------------------------- | ------ |
| A    | Prompt template + `\|` chain runs and prints two answers              | 40     |
| B    | Agent calls the EMI tool correctly and replies with the answer        | 30     |
| C    | Your chosen extra feature works                                       | 15     |
| —   | Short README answers the 4 questions                                   | 15     |

**Passing score: 60 / 100.**

### Partial credit is normal

- Part A working alone = 40 points (already close to passing with the README).
- If the tool is *defined* with `@tool` correctly but the agent step is missing,
  you still earn most of Part B.

---

## Rules

- ✅ You may use your notes.
- ✅ Ask the instructor if you are stuck for more than 10 minutes.
- ❌ Do not have someone else write the whole file for you.

## Common mistakes to avoid

- Mixing up the message classes — use `SystemMessage`/`HumanMessage` for a direct
  model call. Inside `agent.invoke`, use the `{"role": "user", "content": ...}`
  message dict.
- Forgetting the `@tool` decorator, so the agent cannot see the function.
- Forgetting to read the final answer from `result["messages"][-1].content`.
- Leaving the `{question}` placeholder unfilled — always call
  `chain.invoke({"question": "..."})`.
- Not having `OPENROUTER_API_KEY` in your `.env` file.
