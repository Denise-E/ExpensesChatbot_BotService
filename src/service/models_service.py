import time
import asyncio
from src.models.chains_registry import (
    is_expense_pipeline,
    expense_extraction_pipeline,
    category_classification_pipeline
)
from src.data.schemas import ExtractedExpense, CategoryClassification, ExpenseClassification
from src.utils.logger import logger


class ModelsService:

    @classmethod
    async def is_expense(cls, text: str) -> ExpenseClassification:
        logger.info("Validating expense with model")
        start = time.perf_counter()
        is_expense = await is_expense_pipeline.ainvoke({"message": text})
        end = time.perf_counter()
        logger.info(f"Model 1 (¿is a expense?): {end - start:.2f} seconds")
        return is_expense

    @classmethod
    async def get_expense_values(cls, expense: str) -> ExtractedExpense:
        logger.info("Getting expense values with model")
        start = time.perf_counter()
        expense_values = await expense_extraction_pipeline.ainvoke({"message": expense})
        end = time.perf_counter()
        logger.info(f"Model 2 (extraction): {end - start:.2f} seconds")
        return expense_values

    @classmethod
    async def get_expense_category(
            cls, expense_description: str
    ) -> CategoryClassification:
        logger.info("Getting expense category with model")

        start = time.perf_counter()
        expense_category = await category_classification_pipeline.ainvoke(
            {"message": expense_description}
        )
        end = time.perf_counter()

        logger.info(f"Model 3 (category): {end - start:.2f} seconds")
        return expense_category

    @classmethod
    async def extract_and_categorize(cls, expense: str):
        """
        Executes two methods at the same time
        """
        values_task = cls.get_expense_values(expense)
        category_task = cls.get_expense_category(expense)
        return await asyncio.gather(values_task, category_task)
