import asyncio
import sys

from src.data.test_data.is_expense_model_examples import is_expense_examples
from src.models.chains_registry import is_expense_pipeline
from src.utils.logger import logger

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    passed = 0
    for i, example in enumerate(is_expense_examples, start=1):
        try:
            result = await is_expense_pipeline.ainvoke({"message": example["input"]})
            expected = example["expected"]["is_expense"]
            received = result.is_expense

            if received == expected:
                logger.info(f"[{i}] ✅ OK | Input: {example['input']} | Result {received}")
                passed += 1
            else:
                logger.warning(f"[{i}] ❌ FAIL | Input: {example['input']} | Result {received}")
                logger.info(f"    ➤ Esperado: {expected}, Recibido: {received}")
        except Exception as e:
            logger.warning(f"[{i}] ❌ ERROR | Input: {example['input']}")
            logger.warning(f"    ➤ Excepción: {e}")

    examples_quantity = len(is_expense_examples)
    percentage = passed*100/examples_quantity
    logger.info(f"Successfull tests: {passed} out of {examples_quantity} - Equals a {round(percentage, 2)}% "
                f"assertion")

asyncio.run(main())
