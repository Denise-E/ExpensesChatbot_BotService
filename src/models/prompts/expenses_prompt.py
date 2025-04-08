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

2. **If `is_expense` is true**, extract: - "amount": the total spent, as a string. - If the original amount is an 
integer, format it as `"X.0"` (e.g., `"20"` → `"20.0"`) **It can never end with two consecutive zeros**. - If the 
amount has decimals, retain **all the decimals digit**, omitting trailing zeros (e.g., `"20.5"` → `"20.5"`, 
`"30.55"` → `"30.55"`). - "description": short summary (e.g., "Lunch", "Netflix subscription")

If `is_expense` is false, set amount and description to `null`.

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
  "amount": "string or null only if is_expense is false",
  "description": "string or null only if is_expense is false",
  "category": "chosen category from the list or null only if is_expense is false",
  "category_reason": "string or null only if is_expense is false"
}}

Message: "Had sushi with friends last night, 10 bucks and it was so good!"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed food expense",
  "amount": "10.0",
  "description": "Had sushi with friends",
  "category": "Food",
  "category_reason": "Mentions having sushi, which is a food expense"
}}

Message: "Took an Uber to the airport for 50.5 dollars "
Response: {{
  "is_expense": true,
  "reason": "Describes a transportation expense already completed",
  "amount": "50.5",
  "description": "Uber ride to the airport",
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

Message: "50 bucks. Bought new running shoes from Nike"
Response: {{
  "is_expense": true,
  "reason": "Describes a completed purchase",
  "amount": "50.0",
  "description": "Bought running shoes from Nike",
  "category": "Shopping",
  "category_reason": "Purchase of shoes falls under shopping"
}}

Message: "Sent $300 to my savings account"
Response: {{
  "is_expense": true,
  "reason": "Mentions a completed transfer to savings",
  "amount": "300.0",
  "description": "Transfer to savings account",
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
