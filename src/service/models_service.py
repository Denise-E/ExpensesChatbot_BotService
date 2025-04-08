import time

from src.data.categories import CATEGORIES
from src.data.schemas import ExpenseModelOutput
from src.models.chains_registry import expense_model_pipeline
from src.utils.logger import logger

categories_str = ", ".join(CATEGORIES)


class ModelsService:
    @classmethod
    def analyze_expense_model(cls, message: str) -> ExpenseModelOutput:
        logger.info("Analyzing expense - Executing LLM model")
        start = time.perf_counter()
        result = expense_model_pipeline.invoke({
            "message": message,
            "categories": categories_str
        })
        end = time.perf_counter()

        logger.info(f"Expense Model Execution: {end - start:.2f} seconds")
        return result
