from langchain_core.prompts import PromptTemplate

data_analyzer_prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an assistant that extracts expense details from user messages.

Analyze the message and extract:
- amount: the total numeric amount spent (e.g., 1500). If no amount is found, return null.
- description: a short description of the item, service, or reason for the expense (e.g., "a new phone", "lunch", "Netflix subscription").

Respond only with a JSON object.

Message: "{message}"
"""
)
