import asyncio
import sys

from src.data.test_data.expense_category_classifier_examples import expense_category_classifier_examples
from src.models.chains_registry import expense_category_classification_pipeline
from src.utils.logger import logger

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    passed = 0
    for i, example in enumerate(expense_category_classifier_examples, start=1):
        try:
            result = await expense_category_classification_pipeline.ainvoke({"message": example["input"]})
            expected = example["expected"]["category"]
            received = result.category

            if received == expected:
                logger.info(f"[{i}] ✅ OK | Input: {example['input']} | Result {received}")
                passed += 1
            else:
                logger.warning(f"[{i}] ❌ FAIL | Input: {example['input']} | Result {received}")
                logger.info(f"    ➤ Esperado: {expected}, Recibido: {received}")
        except Exception as e:
            logger.warning(f"[{i}] ❌ ERROR | Input: {example['input']} - {result.description}")
            logger.warning(f"    ➤ Excepción: {e}")

    examples_quantity = len(expense_category_classifier_examples)
    percentage = passed*100/examples_quantity
    logger.info(f"Successfull tests: {passed} out of {examples_quantity} - Equals a {round(percentage, 2)}% "
                f"assertion")

asyncio.run(main())
