import datetime

from pydantic import BaseModel, Field
from typing import Optional


# LLM Models Schemas

class ExpenseClassification(BaseModel):
    is_expense: bool = Field(..., description="Whether the message contains an expense")
    reason: str = Field(..., description="Justification for the classification decision")


class ExtractedExpense(BaseModel):
    amount: Optional[float] = Field(None, description="The amount of money spent")
    description: Optional[str] = Field(None, description="What the expense was for")


class CategoryClassification(BaseModel):
    category: str = Field(..., description="Detected category for the expense")
    reason: str = Field(..., description="Justification for the selected category")


# Create Expense Endpoint Schemas

class CreateExpenseInput(BaseModel):
    telegram_id: str = Field(..., description="Telegram ID of the user")
    message: str = Field(..., description="Message sent by the user that might contain expense information")


class CreateExpenseOutput(BaseModel):
    user_id: int = Field(..., description="Internal ID of the user in the database")
    amount: float = Field(..., description="Amount extracted from the message")
    description: str = Field(..., description="Description of the expense extracted from the message")
    category: str = Field(..., description="Category assigned to the expense")
    added_at: datetime.datetime = Field(..., description="Datetime when the expense was added")


# Create User Endpoint Schemas

class CreateUserInput(BaseModel):
    telegram_id: str = Field(..., description="Telegram ID of the user to be registered")


class CreateUserOutput(BaseModel):
    id: int = Field(..., description="Internal ID of the created user")
    telegram_id: str = Field(..., description="Telegram ID of the created user")
