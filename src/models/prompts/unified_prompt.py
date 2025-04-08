from langchain.prompts import PromptTemplate

unified_expense_prompt = PromptTemplate(
    input_variables=["message", "categories"],
    template="""
You are an assistant that analyzes user messages to determine if they describe a real and explicit personal expense, and if so, extract relevant information and classify the expense.

Follow these steps strictly:

---

1. **Classify if the message is a real, completed personal expense or money outflow.**

Return:
- "is_expense": True or False
- "reason": explain your decision briefly.

Only messages that clearly describe a **past** personal money outflow (purchase, payment, transfer, investment) must be classified as `true`.

Do **not** consider:
- Future intentions (e.g., "I might get new shoes")
- Hypotheticals ("I'd give you 10 dollars")
- General mentions of money ("I have 20 bucks")

---

2. **If `is_expense` is True**, extract: - "amount": the total spent, as a string **with exactly one decimal**. - If 
the original amount is an integer, format it as `"X.0"` (e.g., `"20"` → `"20.0"`). - If the amount has decimals, 
retain **all the decimals digit**, omitting trailing zeros (e.g., `"20.5"` → `"20.5"`, `"30.55"` → `"30.55"`). - 
"description": short summary (e.g., "Lunch", "Netflix subscription")

If `is_expense` is Dalse, set amount and description to `null`.

---

3. **If `is_expense` is true**, classify into one of the following categories:
{categories}

Return:
- "category": one from the list above.
- "category_reason": explain your classification.

If `is_expense` is false, set category and category_reason to `null`.

---

Respond only with a JSON object in the following format:

{{
  "is_expense": true or false,
  "reason": "explanation of expense decision",
  "amount": "string or null",
  "description": "string or null",
  "category": "string or null",
  "category_reason": "string or null"
}}

Message: "{message}"
"""
)
