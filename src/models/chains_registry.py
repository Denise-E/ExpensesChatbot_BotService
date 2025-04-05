from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_ollama import ChatOllama

from src.data.schemas import ExtractedExpense, CategoryClassification, ExpenseClassification
from src.models.prompts.category_classifier_prompt import category_classifier_prompt
from src.models.prompts.expense_data_analyzer import data_analyzer_prompt
from src.models.prompts.is_expense_prompt import is_expense_prompt

# LLMs initializations
llm_mistral = ChatOllama(model="mistral")
llm_llama3 = ChatOllama(model="llama3")

# Chains
extract_chain: RunnableSequence = data_analyzer_prompt | llm_mistral
category_chain: RunnableSequence = category_classifier_prompt | llm_mistral
is_expense_chain: RunnableSequence = is_expense_prompt | llm_mistral

# Parsers
extract_parser = PydanticOutputParser(pydantic_object=ExtractedExpense)
category_parser = PydanticOutputParser(pydantic_object=CategoryClassification)
expense_validator_parser = PydanticOutputParser(pydantic_object=ExpenseClassification)

# Pipelines (prompt | model | parser)
expense_extraction_pipeline = data_analyzer_prompt | llm_mistral | extract_parser
category_classification_pipeline = category_classifier_prompt | llm_mistral | category_parser
is_expense_pipeline = is_expense_prompt | llm_llama3 | expense_validator_parser
