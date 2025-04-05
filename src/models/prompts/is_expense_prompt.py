from langchain_core.prompts import PromptTemplate

is_expense_prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an intelligent assistant that analyzes messages to identify personal expenses.

Determine if the message describes a **real and explicit** personal expense — not just a mention of money, a joke, or a future intention.

Respond only with a JSON object with:
- is_expense: true if the message clearly describes a completed or definite personal expense (e.g., "I bought X", "I paid Y"); false otherwise.
- reason: a brief explanation justifying your decision.

Examples of messages that should return **false**:
- Casual greetings with numbers (e.g., "Hey, how are you? I have 20 bucks")
- Future intentions (e.g., "I want to buy...", "I'm planning to get...")
- Jokes or subjective statements with money (e.g., "I could give u 20 dollars just because you're a good person")

Message: "{message}"
"""
)
