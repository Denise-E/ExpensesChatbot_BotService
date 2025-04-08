from langchain_core.prompts import PromptTemplate

is_expense_prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an assistant that analyzes user messages to determine whether they describe a real and explicit **personal expense or money outflow**.

Analyze the message and classify:
- is_expense: true if the message clearly describes a completed personal expense or money outflow (e.g., "I bought a backpack for 30 dollars", "Paid rent today", "Deposited 500 into my investment account"); false otherwise.
- reason: a brief explanation justifying your decision (e.g., "Describes a past payment", "Mentions a future intention", "Just a casual comment about money").

Respond only with a JSON object using this format:
{{
  "is_expense": true or false,
  "reason": "your explanation here"
}}

Messages that should be classified as **false** include:
- Casual mentions of money (e.g., "I have 20 bucks", "Still waiting for my 50")
- Future intentions (e.g., "I'm planning to get new shoes", "I might spend 100 on that")
- Hypothetical or playful comments (e.g., "I'd give you 10 dollars just for showing up")
- Messages without any money outflow (e.g., "Netflix is too expensive")

Clarifications:
- Expenses include not only purchases or bills, but also **any movement of money out of the user's account**, such as transfers, deposits to other personal accounts, or investments.
- The message must refer to an **action that already happened**, not something intended or hypothetical.

Message: "{message}"
"""
)

