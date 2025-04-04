from src.models.expenses_clasificator import build_expense_classification_chain


class ModelsService:

    @classmethod
    def is_expense(cls, text: str) -> bool:
        chain = build_expense_classification_chain()
        is_expense = chain.invoke({"message": text})
        return is_expense



