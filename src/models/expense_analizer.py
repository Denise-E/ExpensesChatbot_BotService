from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import PydanticOutputParser

from src.data.schemas import ExtractedExpense

extract_prompt = PromptTemplate(
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

# mistral model is faster and lighter than llama3 model
llm = ChatOllama(model="mistral")
extract_chain = LLMChain(llm=llm, prompt=extract_prompt)

parser = PydanticOutputParser(pydantic_object=ExtractedExpense)


def build_expense_extraction_chain():
    return extract_prompt | llm | parser
