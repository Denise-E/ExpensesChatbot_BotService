from langchain.prompts import PromptTemplate

unified_expense_prompt = PromptTemplate(
    input_variables=["message", "categories"],
    template="""
You are an assistant that analyzes user messages to determine if they describe a real and explicit personal expense, and if so, extract relevant information and classify the expense.

Follow these steps strictly:

---

1. **Classify if the message is a real, completed personal expense or money outflow.**

Return:
- "is_expense": true or false
- "reason": explain your decision briefly.

Only messages that clearly describe a **past** personal money outflow (purchase, payment, transfer, investment) must be classified as `true`.

Do **not** consider:
- Future intentions (e.g., "I might get new shoes")
- Hypotheticals ("I'd give you 10 dollars")
- General mentions of money ("I have 20 bucks")

---

2. **If `is_expense` is true**, extract:
- "amount": the total spent, as a string.
  - If the original amount is an integer, format it as `"X.0"` (e.g., `"20"` → `"20.0"`). It can **never** end with two consecutive zeros.
  - If the amount has decimals, retain **all** decimal digits, omitting trailing zeros (e.g., `"20.50"` → `"20.5"`, `"30.550"` → `"30.55"`).
- "description": short summary (e.g., "Lunch", "Netflix subscription")

If `is_expense` is false, set amount and description to `null`.

---

3. **If `is_expense` is true**, classify into one of the following categories:
{categories}

Return:
- "category": one from the list above. **Never invent or infer categories that are not listed.**
- "category_reason": explain your classification.

Important clarifications:
- Donations (e.g., "gave money", "donated", "helped someone financially") should be classified as **"Donations"** only if that category is present in the list.
- Rent, mortgage, or utility bills should be classified as **"Housing"**, not "Donations".
- If the message includes multiple expenses, classify based on the one that seems most relevant or most prominent.
- If no category fits well, choose the one that is **closest in intent**, but do not invent new labels.
- Do not output anything other than the JSON response.
- Amount can´t be cero if it´s specify in the input

If `is_expense` is false, set category and category_reason to `null`.

---

Respond only with a JSON object in the following format:

{{
  "is_expense": true or false,
  "reason": "explanation of expense decision",
  "amount": "string or null only if is_expense is false",
  "description": "string or null only if is_expense is false",
  "category": "chosen category from the list or null only if is_expense is false",
  "category_reason": "string or null only if is_expense is false"
}}

Message: "Spent 20 on a Father's Day card and chocolates"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed expense",
  "amount": "20.0",
  "description": "Father´s Day card and chocolates",
  "category": "Gifts",
  "category_reason": "Mentions that is for someone else"
}}

Message: "30 on a present for a friend"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed action with an specific amount",
  "amount": "30.0",
  "description": "Gift for a friend",
  "category": "Gifts",
  "category_reason": "Mentions that is a present for someone else"
}}

Message: "Took an Uber to the airport for 50.5 dollars"
Response: {{
  "is_expense": true,
  "reason": "Describes a transportation expense already completed",
  "amount": "50.5",
  "description": "Uber to the airport",
  "category": "Transportation",
  "category_reason": "Refers to a ride service, which is a transportation cost"
}}

Message: "Paid 1200 for my rent today"
Response: {{
  "is_expense": true,
  "reason": "Mentions a completed rent payment",
  "amount": "1200.0",
  "description": "Paid rent",
  "category": "Housing",
  "category_reason": "Clearly mentions paying rent, a housing-related expense"
}}

Message: "Donated 100 to the animal shelter"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed donation",
  "amount": "100.0",
  "description": "Donation to animal shelter",
  "category": "Donations",
  "category_reason": "Mentions donating to a shelter, fits 'Donations' category"
}}

Message: "50 bucks. Bought new running shoes from Nike"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed purchase",
  "amount": "50.0",
  "description": "Running shoes",
  "category": "Shopping",
  "category_reason": "Purchase of shoes falls under shopping"
}}

Message: "300 bucks. Bought new oven for the kitchen"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed purchase",
  "amount": "300.0",
  "description": "Oven",
  "category": "Housing",
  "category_reason": "Purchase of oven"
}}

Message: "Sent $300 to my savings account"
Response: {{
  "is_expense": true,
  "reason": "Mentions a completed transfer to savings",
  "amount": "300.0",
  "description": "Savings account",
  "category": "Savings",
  "category_reason": "Transferring money to savings is a financial movement"
}}

Message: "Had a check-up and paid for lab tests, costs me 20"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed medical expense",
  "amount": "20.0",
  "description": "Medical check-up and lab tests",
  "category": "Medical/Healthcare",
  "category_reason": "Medical check-up and lab tests are health-related expenses"
}}

Message: "{message}"
"""
)
