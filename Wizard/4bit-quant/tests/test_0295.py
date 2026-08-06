python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0295 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'id': [1, 2, 3, 4], 'age': [25, 30, 35, 40], 'income': [50000, 60000, 70000, 80000]})
    expected_output = pd.DataFrame({'age': [-1.3416407864998738, 0.0, 1.3416407864998738], 'income': [-1.224744871391589, 0.0, 1.224744871391589]}, index=[1, 2, 3])
    assert task_func(df).equals(expected_output)

    # Test case 2: Test with invalid input
    df = pd.DataFrame({'id': [1, 2, 3, 4], 'age': [25, 30, 35, 40], 'income': [50000, 60000, 70000, '80000']})
    with pytest.raises(ValueError):
        task_func(df)