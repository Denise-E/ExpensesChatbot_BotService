from src.data.schemas import ExtractedExpense, CategoryClassification
from src.models.expense_analizer import build_expense_extraction_chain
from src.models.expense_category_clasifier import build_category_classification_chain
from src.models.expenses_clasificator import build_expense_classification_chain


class ModelsService:

    @classmethod
    def is_expense(cls, text: str) -> bool:
        chain = build_expense_classification_chain()
        is_expense = chain.invoke({"message": text})
        return is_expense

    @classmethod
    def get_expense_values(cls, expense: str) -> ExtractedExpense:
        chain = build_expense_extraction_chain()
        expense_values = chain.invoke(expense)
        return expense_values

    @classmethod
    def get_expense_category(cls, expense_description: str) -> CategoryClassification:
        chain = build_category_classification_chain()
        expense_category = chain.invoke(expense_description)
        return expense_category
