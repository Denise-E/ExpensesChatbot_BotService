from pydantic import BaseModel, Field
from typing import Optional


class ExpenseClassification(BaseModel):
    is_expense: bool
    reason: str


class ExtractedExpense(BaseModel):
    amount: Optional[float] = Field(None, description="The amount of money spent")
    description: Optional[str] = Field(None, description="What the expense was for")


class CategoryClassification(BaseModel):
    category: str
    reason: str
