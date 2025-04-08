from src.data.categories import CATEGORIES
from src.data.test_data.expense_examples import expense_examples
from src.models.chains_registry import expense_model_pipeline
from src.utils.logger import logger

categories_str = ", ".join(CATEGORIES)


def main():
    passed = 0
    for i, example in enumerate(expense_examples, start=1):
        try:
            result = expense_model_pipeline.invoke({"message": example["input"], "categories": categories_str})
            expected_is_expense = example["expected"]["is_expense"]
            expected_amount = example["expected"]["amount"]
            expected_category = example["expected"]["category"]
            received_is_expense = result.is_expense
            received_amount = result.amount
            received_category = result.category

            is_expense_ok = received_is_expense == expected_is_expense
            amount_ok = received_amount == expected_amount
            category_ok = received_category == expected_category

            if expected_is_expense:
                all_ok = is_expense_ok and amount_ok and category_ok
            else:
                all_ok = is_expense_ok

            if all_ok:
                passed += 1
                logger.info(f"[{i}] ✅ PASSED | Input: {example['input']}")
            else:
                logger.warning(f"[{i}] ❌ FAILED | Input: {example['input']}")
                logger.warning(f"    ➤ Expected is_expense: {expected_is_expense}, Got: {received_is_expense}")
                if expected_is_expense:
                    logger.warning(f"    ➤ Expected amount: {expected_amount}, Got: {received_amount}")
                    logger.warning(f"    ➤ Expected category: {expected_category}, Got: {received_category}")

        except Exception as e:
            logger.warning(f"[{i}] ❌ ERROR | Input: {example['input']}")
            logger.warning(f"    ➤ Excepción: {e}")

    examples_quantity = len(expense_examples)
    percentage = passed * 100 / examples_quantity
    logger.info(f"Successfull tests: {passed} out of {examples_quantity} - Equals a {round(percentage, 2)}% "
                f"assertion")


main()
