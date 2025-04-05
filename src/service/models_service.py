from src.data.schemas import ExtractedExpense, CategoryClassification, ExpenseClassification
from src.models.chains_registry import (
    is_expense_pipeline,
    expense_extraction_pipeline,
    category_classification_pipeline,
)


class ModelsService:

    @classmethod
    def is_expense(cls, text: str) -> ExpenseClassification:
        return is_expense_pipeline.invoke({"message": text})

    @classmethod
    def get_expense_values(cls, expense: str) -> ExtractedExpense:
        return expense_extraction_pipeline.invoke({"message": expense})

    @classmethod
    def get_expense_category(cls, expense_description: str) -> CategoryClassification:
        return category_classification_pipeline.invoke({"message": expense_description})
