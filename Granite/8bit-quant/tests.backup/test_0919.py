import pandas as pd
import pytest
import re
from src_0919 import task_func

# Sample data and mapping
data = {
    'col1': ['ABC', 'XYZ', 'PQR'],
    'col2': ['DEF', 'GHI', 'JKL']
}
mapping = {'ABC': '123', 'XYZ': '789'}

# Expected output after replacing acronyms
expected_output = {
    'col1': ['123', '789', 'PQR'],
    'col2': ['DEF', 'GHI', 'JKL']
}

# Test if the function returns the expected output
def test_task_func():
    df = task_func(data, mapping)
    assert df.to_dict() == expected_output

# Test if the function raises an exception for invalid input
def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('invalid_data', mapping)