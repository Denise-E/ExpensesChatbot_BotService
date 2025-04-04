from pydantic import BaseModel


class ExpenseClassification(BaseModel):
    is_expense: bool
    reason: str
