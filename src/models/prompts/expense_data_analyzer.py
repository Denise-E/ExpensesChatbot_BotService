from langchain_core.prompts import PromptTemplate

data_analyzer_prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an assistant that extracts expense details from user messages.

Return a JSON object with: - "amount": the total amount spent, written as a **string** with decimal point (e.g., 
"8.0", "0.05", "3.75", "1.50", "30.50"). Use as many decimal digits as necessary (e.g., "0.05" for 5 cents). If the 
amount is in cents, convert to dollars. Multiply only if the total is not already mentioned. - "description": a 
concise summary of the expense (e.g., "Netflix subscription", "Books", "Lunch"). Only the first letter in capital and 
without declarations between parenthesis.

Format:
{{
  "amount": "string or null",
  "description": "string"
}}

Examples:
"5 cents, to enter the museum" → amount: "0.05", description: "Museum"
"Went bowling and paid for two rounds 10 bucks" → amount: "10.0", description: "Bowling"
"I bought 2 coffees at 3.75 bucks each" → amount: "7.5", description: "Coffees"
"Grabbed 10 stamps, 0.6 each" → amount: "6.0", description: "Stamps"
"I got 4 school textbooks for 15 bucks each" -> amount: "60.0", description: "School textbooks"
"Sushi delivered for dinner, 80 " → amount: "80.0", description: "Sushi"
"Moved 1500 bucks to a high-yield savings account" → amount: "1500.0", description: "Savings account"

Message: "{message}"
"""
)

