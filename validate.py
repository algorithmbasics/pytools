# File: _validate.py

# libraries & dependencies
# Standard libraries
import os
import sys
import asyncio
import pandas as pd
from typing import Any, Optional

# Third-party libraries
# None

# Adjusting the path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Local imports
from code.utils.custom_logger import ensure_logger_setup, get_logger # type: ignore

# glocal variables
# None


def validate(
    obj: Any,
    dict_instance: Optional[bool] = None,
    list_instance: Optional[bool] = None,
    tuple_instance: Optional[bool] = None,
    str_instance: Optional[bool] = None,
    int_instance: Optional[bool] = None,
    float_instance: Optional[bool] = None,
    bool_instance: Optional[bool] = None,
    pd_dataframe_instance: Optional[bool] = None,
    pd_series_instance: Optional[bool] = None,
    is_not_None: Optional[bool] = None,
    is_not_empty: Optional[bool] = None,
    is_numeric: Optional[bool] = None,
) -> bool:
    """
    Universal validator for generic Python objects.

    Validates object using various optional flags.
    Returns True only if all *enabled* conditions pass.

    Priority:
    1. Check for is_not_None
    2. Check for is_not_empty
    3. Then check types and other flags

    Args:
        obj (Any): The object to validate.
        (Optional flags follow...)

    Returns:
        bool: True if all validations pass. False otherwise.
    """
    logger = get_logger()

    status_check: bool = True

    # Priority 1: Null check
    if is_not_None and obj is None:
        logger.info(f"Object is None. Type: {type(obj).__name__}, {obj=}, {is_not_None=}")
        status_check = False
    else:
        logger.info(f"Object is not None. Type: {type(obj).__name__}, {is_not_None=}")

    # Priority 2: Emptiness check
    if is_not_empty:
        if obj is None:
            status_check = False
        if hasattr(obj, '__len__'):
            if len(obj) == 0:
                logger.info(f"Object is empty. Type: {type(obj).__name__}, {obj=}, {is_not_empty=}")
                status_check = False
            else:
                logger.info(f"Object is not empty. Type: {type(obj).__name__}, {is_not_empty=}")

    if not status_check:
        return False

    # Priority 3: Type checks (run only if enabled)
    if dict_instance:
        if not isinstance(obj, dict):
            logger.info(f"Object is not dict. Type: {type(obj).__name__}, {obj=}, {dict_instance=}")
            status_check = False
        else:
            logger.info(f"Object is dict. Type: {type(obj).__name__}, {obj=}, {dict_instance=}")

    if list_instance:
        if not isinstance(obj, list):
            logger.info(f"Object is not list. Type: {type(obj).__name__}, {obj=}, {list_instance=}")
            status_check = False
        else:
            logger.info(f"Object is list. Type: {type(obj).__name__}, {obj=}, {list_instance=}")

    if tuple_instance:
        if not isinstance(obj, tuple):
            logger.info(f"Object is not tuple. Type: {type(obj).__name__}, {obj=}, {tuple_instance=}")
            status_check = False
        else:
            logger.info(f"Object is tuple. Type: {type(obj).__name__}, {obj=}, {tuple_instance=}")

    if str_instance:
        if not isinstance(obj, str):
            logger.info(f"Object is not string. Type: {type(obj).__name__}, {obj=}, {str_instance=}")
            status_check = False
        else:
            logger.info(f"Object is string. Type: {type(obj).__name__}, {obj=}, {str_instance=}")

    if int_instance:
        if not isinstance(obj, int):
            logger.info(f"Object is not integer. Type: {type(obj).__name__}, {obj=}, {int_instance=}")
            status_check = False
        else:
            logger.info(f"Object is integer. Type: {type(obj).__name__}, {obj=}, {int_instance=}")

    if float_instance:
        if not isinstance(obj, float):
            logger.info(f"Object is not float. Type: {type(obj).__name__}, {obj=}, {float_instance=}")
            status_check = False
        else:
            logger.info(f"Object is float. Type: {type(obj).__name__}, {obj=}, {float_instance=}")

    if bool_instance:
        if not isinstance(obj, bool):
            logger.info(f"Object is not bool. Type: {type(obj).__name__}, {obj=}, {bool_instance=}")
            status_check = False
        else:
            logger.info(f"Object is bool. Type: {type(obj).__name__}, {obj=}, {bool_instance=}")

    if pd_dataframe_instance:
        if not isinstance(obj, pd.DataFrame):
            logger.info(f"Object is not pd.DataFrame. Type: {type(obj).__name__}, {pd_dataframe_instance=}")
            status_check = False
        elif obj.empty:
            logger.info(f"Object is pd.DataFrame but empty. Type: {type(obj).__name__}, head:\n{obj.head()}")
            status_check = False
        else:
            logger.info(f"Object is non-empty pd.DataFrame. Type: {type(obj).__name__}, head:\n{obj.head()}")

    if pd_series_instance:
        if not isinstance(obj, pd.Series):
            logger.info(f"Object is not pd.Series. Type: {type(obj).__name__}, {pd_series_instance=}")
            status_check = False
        elif obj.empty:
            logger.info(f"Object is pd.Series but empty. Type: {type(obj).__name__}, head:\n{obj.head()}")
            status_check = False
        else:
            logger.info(f"Object is non-empty pd.Series. Type: {type(obj).__name__}, head:\n{obj.head()}")

    if is_numeric:
        if not isinstance(obj, (int, float)):
            logger.info(f"Object is not numeric. Type: {type(obj).__name__}, {obj=}, {is_numeric=}")
            status_check = False
        else:
            logger.info(f"Object is numeric. Type: {type(obj).__name__}, {obj=}, {is_numeric=}")
    return status_check

# Example usage:
if __name__ == "__main__":
    # Validate a dictionary
    print(validate({"key": "value"}, dict_instance=True))  # True

    # Validate a list
    print(validate([1, 2, 3], list_instance=True))  # True

    # Validate a string
    print(validate("Hello", str_instance=True))  # True

    # Validate an integer
    print(validate(42, int_instance=True))  # True

    # Validate a float
    print(validate(3.14, float_instance=True))  # True

    # Validate a boolean
    print(validate(True, bool_instance=True))  # True

    # Validate a non-empty string
    print(validate("Hello", str_instance=True, is_not_empty=True))  # True

    # Validate an empty string
    print(validate("", str_instance=True, is_not_empty=True))  # False

    # Validate a numeric value
    print(validate(5, int_instance=True, is_numeric=True))  # True

    # Validate a tuple
    print(validate((1, 2), tuple_instance=True))  # True

    # Validate a pandas DataFrame
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print(validate(df, pd_dataframe_instance=True))  # True

    # Validate a pandas Series
    series = pd.Series([1, 2, 3])
    print(validate(series, pd_series_instance=True))  # True
