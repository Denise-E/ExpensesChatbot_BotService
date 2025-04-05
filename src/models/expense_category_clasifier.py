from pydantic import BaseModel
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_community.chat_models import ChatOllama
from src.data.categories import CATEGORIES
from src.data.schemas import CategoryClassification

parser = PydanticOutputParser(pydantic_object=CategoryClassification)
categories_str = ", ".join(CATEGORIES)

prompt = PromptTemplate(
    input_variables=["description"],
    template=f"""
You are a financial assistant trained to classify expense descriptions into categories.

Given a description of a personal expense, classify it into one of the following categories:
{categories_str}

Respond ONLY with a JSON object containing:
- category: the chosen category from the list
- reason: a short explanation of your choice

Description: "{{description}}"
""",
)

llm = ChatOllama(model="mistral")


def build_category_classification_chain():
    return prompt | llm | parser
