from langchain_core.output_parsers import PydanticOutputParser
from langchain_community.chat_models import ChatOllama
from src.data.schemas import ExpenseClassification
from langchain_core.prompts import PromptTemplate

# Prompt
prompt = PromptTemplate(
    input_variables=["message"],
    template="""
You are an intelligent assistant that analyzes messages to identify personal expenses.

Determine if the message describes a **real and explicit** personal expense — not just a mention of money, a joke, or a future intention.

Respond only with a JSON object with:
- is_expense: true if the message clearly describes a completed or definite personal expense (e.g., "I bought X", "I paid Y"); false otherwise.
- reason: a brief explanation justifying your decision.

Examples of messages that should return **false**:
- Casual greetings with numbers (e.g., "Hey, how are you? 20 pesos")
- Future intentions (e.g., "I want to buy...", "I'm planning to get...")
- Jokes or subjective statements with money (e.g., "20 pesos because you're ugly")

Message: "{message}"
"""
)


# Ollama Model
llm = ChatOllama(model="llama3")

# Pydantic parser
parser = PydanticOutputParser(pydantic_object=ExpenseClassification)

# Chain
def build_expense_classification_chain():
    return prompt | llm | parser
