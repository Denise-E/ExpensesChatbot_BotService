from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


# LLM Models Schemas
class ExpenseModelOutput(BaseModel):
    is_expense: bool = Field(..., description="Whether the message contains an expense")
    reason: str = Field(..., description="Justification for the classification decision")
    amount: Optional[str] = Field(None, description="The amount of money spent")
    description: Optional[str] = Field(None, description="What the expense was for")
    category: Optional[str] = Field(None, description="Detected category for the expense")
    category_reason: Optional[str] = Field(None, description="Justification for the selected category")


# Create Expense Endpoint Schemas

class CreateExpenseInput(BaseModel):
    telegram_id: str = Field(..., description="Telegram ID of the user")
    message: str = Field(..., description="Message sent by the user that might contain expense information")


class CreateExpenseOutput(BaseModel):
    user_id: int = Field(..., description="Internal ID of the user in the database")
    amount: str = Field(..., description="Amount extracted from the message")
    description: str = Field(..., description="Description of the expense extracted from the message")
    category: str = Field(..., description="Category assigned to the expense")
    added_at: datetime = Field(..., description="Datetime when the expense was added")


# Get All User Expenses Endpoint Schemas

class Expense(BaseModel):
    id: int = Field(..., description="Unique identifier of the expense")
    user_id: int = Field(..., description="ID of the user who added the expense")
    description: str = Field(..., description="Description of the expense")
    amount: str = Field(..., description="Amount spent", example=59.99)
    category: str = Field(..., description="Category of the expense", example="Food")
    added_at: datetime = Field(..., description="Timestamp when the expense was added")


class GetAllUserExpensesOutput(BaseModel):
    expenses: List[Expense] = Field(..., description="List of user expenses")


# Create User Endpoint Schemas

class CreateUserInput(BaseModel):
    telegram_id: str = Field(..., description="Telegram ID of the user to be registered")


class CreateUserOutput(BaseModel):
    id: int = Field(..., description="Internal ID of the created user")
    telegram_id: str = Field(..., description="Telegram ID of the created user")
