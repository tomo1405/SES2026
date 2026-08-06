import pytest
from src_0550 import task_func
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    base64_string = task_func(df)
    assert base64_string == 'MTIzNDU2Nzg5OQ=='