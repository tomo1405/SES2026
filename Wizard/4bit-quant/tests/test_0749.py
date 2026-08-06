python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0749 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'Age': [20, 25, 30, 35], 'Weight': [50, 60, 70, 80]})
    age = 30
    weight = 60
    expected_result = pd.DataFrame({'Age': [25, 30], 'Weight': [60, 70]}, index=[1, 2])
    result = task_func(df, age, weight)
    assert result.equals(expected_result)

    # Test case 2: Test with empty DataFrame
    df = pd.DataFrame({'Age': [20, 25, 30, 35], 'Weight': [50, 60, 70, 80]})
    age = 40
    weight = 70
    expected_result = pd.DataFrame({'Age': [], 'Weight': []})
    result = task_func(df, age, weight)
    assert result.equals(expected_result)

    # Test case 3: Test with invalid input (age > 40)
    df = pd.DataFrame({'Age': [20, 25, 30, 35], 'Weight': [50, 60, 70, 80]})
    age = 45
    weight = 60
    with pytest.raises(ValueError):
        task_func(df, age, weight)

    # Test case 4: Test with invalid input (weight < 50)
    df = pd.DataFrame({'Age': [20, 25, 30, 35], 'Weight': [50, 60, 70, 80]})
    age = 30
    weight = 40
    with pytest.raises(ValueError):
        task_func(df, age, weight)