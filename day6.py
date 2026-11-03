# Day 6 Tasks:
# 1. Debugging and Tracebacks
# 2. Logging
# 3. Reproducible Bug Reports
# 4. Git 
# 5. Code Review Basics

# =======TRACEBACKS=======
print("=====TRACEBACKS=====")


def get_average(numbers):
    if not numbers:
        raise ValueError("numbers list must not be empty")
    return sum(numbers) / len(numbers)

def process_data(data):
    result = get_average(data)
    return result

def main():
    scores = [10,20,30]
    print(process_data(scores))

main()


# OUTPUT

# Traceback (most recent call last):
#   File "F:\Techugo_week2\day6.py", line 22, in <module>
#     main()
#   File "F:\Techugo_week2\day6.py", line 20, in main
#     print(process_data(scores))
#           ^^^^^^^^^^^^^^^^^^^^
#   File "F:\Techugo_week2\day6.py", line 15, in process_data
#     result = get_average(data)
#              ^^^^^^^^^^^^^^^^^
#   File "F:\Techugo_week2\day6.py", line 12, in get_average
#     return total / len(numbers)
#            ~~~~~~^~~~~~~~~~~~~~
# ZeroDivisionError: division by zero

# to get it fixed fill some numbers in the scores list to calculate the average


# ==========LOGGING==========

print("======LOGGING========")

import logging

from logging_config import setup_logging

logger = logging.getLogger(__name__)


def get_average(numbers: list[float]) -> float:
    logger.debug("get_average called, numbers=%s", numbers)
    if not numbers:
        logger.error("Empty list is empty, average cannot be calculated")
        raise ValueError("numbers list must not be empty")
    result = sum(numbers) / len(numbers)
    logger.info("Average calculated: %s", result)
    return result


def main() -> None:
    logger.info("App started")
    try:
        get_average([10, 20, 30])                
        # get_average([])                   when the list is empty it gives traceback error for value error
    except ValueError:
        logger.exception("Error found during calculating average")
    logger.info("App Closed")


if __name__ == "__main__":
    setup_logging()   
    main()