python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0295 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'age': [25, 30, 35, 40, 45], 'income': [50000, 60000, 70000, 80000, 90000]})
    expected_output = pd.DataFrame({'age': [-1.3416407864998738, -0.4472136, 0.4472136, 1.3416407864998738], 'income': [-1.224744871391589, -0.5773502691896257, 0.5773502691896257, 1.224744871391589]}, index=[1, 2, 3, 4])
    assert task_func(df).equals(expected_output)

    # Test case 2: Test with invalid input (empty dataframe)
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)