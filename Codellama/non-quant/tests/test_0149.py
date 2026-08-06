import pytest
from src_0149 import task_func
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def test_task_func():
    df = pd.DataFrame({'A': ['a', 'b', 'c', 'd', 'e']})
    column_name = 'A'
    expected_output = pd.DataFrame({'A': [0, 1, 2, 3, 4]})
    output = task_func(df, column_name)
    assert output.equals(expected_output)