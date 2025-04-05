# File: calculate_returns.py

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

    # Priority 1: Null check
    if is_not_None and obj is None:
        return False

    # Priority 2: Emptiness check
    if is_not_empty:
        if obj is None:
            return False
        if hasattr(obj, '__len__'):
            if len(obj) == 0:
                return False

    # Priority 3: Type checks (run only if enabled)
    if dict_instance and not isinstance(obj, dict):
        return False
    if list_instance and not isinstance(obj, list):
        return False
    if tuple_instance and not isinstance(obj, tuple):
        return False
    if str_instance and not isinstance(obj, str):
        return False
    if int_instance and not isinstance(obj, int):
        return False
    if float_instance and not isinstance(obj, float):
        return False
    if bool_instance and not isinstance(obj, bool):
        return False
    if pd_dataframe_instance and not isinstance(obj, pd.DataFrame):
        return False
    if pd_series_instance and not isinstance(obj, pd.Series):
        return False
    if is_numeric and not isinstance(obj, (int, float)):
        return False

    return True
