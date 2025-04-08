from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama

from src.data.schemas import ExpenseModelOutput
from src.models.prompts.unified_prompt import unified_expense_prompt

# LLMs initializations
llm_mistral = ChatOllama(model="mistral")

# Parsers
expense_model_parser = PydanticOutputParser(pydantic_object=ExpenseModelOutput)

# Pipelines (prompt | model | parser)
expense_model_pipeline = unified_expense_prompt | llm_mistral | expense_model_parser
