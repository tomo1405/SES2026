from io import StringIO

import pandas as pd
import pytest
from src_0191 import task_func


def test_task_func_with_stringio():
    csv_input = StringIO('col1,col2\n1,2\n3,4')
    dataframe = task_func(csv_input)
    assert dataframe.equals(pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]}))

def test_task_func_with_file():
    csv_input = 'test_data.csv'
    dataframe = task_func(csv_input)
    assert dataframe.equals(pd.DataFrame({'col1': [1, 3], 'col2': [2, 4]}))

def test_task_func_with_invalid_input():
    csv_input = 'invalid_data.csv'
    with pytest.raises(ValueError):
        task_func(csv_input)