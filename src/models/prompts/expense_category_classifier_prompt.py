from langchain.prompts import PromptTemplate
from src.data.categories import CATEGORIES

categories_str = ", ".join(CATEGORIES)

category_classifier_prompt = PromptTemplate(
    input_variables=["message"],
    template=f"""
You are a financial assistant trained to classify expense descriptions into categories.

Given a description of a personal expense, classify it into one of the following categories:
{categories_str}

Respond ONLY with a JSON object containing:
- category: the chosen category from the list
- reason: a short explanation of your choice

Description: "{{message}}"
""",
)
