from src.data.schemas import ExtractedExpense
from src.models.expense_analizer import build_expense_extraction_chain
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


