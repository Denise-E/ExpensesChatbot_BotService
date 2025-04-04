from langchain_core.output_parsers import PydanticOutputParser
from langchain_community.chat_models import ChatOllama
from src.data.schemas import ExpenseClassification
from langchain_core.prompts import PromptTemplate

# Prompt
prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are a smart assistant that filters expense-related messages.

Given the user message below, determine if it refers to a personal expense.

Respond with a JSON with:
- is_expense: true if it refers to a personal expense else false
- reason: a short explanation

Message: "{message}"
""",
)

# Ollama Model
llm = ChatOllama(model="llama3")

# Pydantic parser
parser = PydanticOutputParser(pydantic_object=ExpenseClassification)

# Chain
def build_expense_classification_chain():
    return prompt | llm | parser
