import pytest
from src_0749 import task_func

def test_task_func():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    age = 10
    weight = 50
    expected_result = pd.DataFrame()
    assert task_func(df, age, weight).equals(expected_result)

    # Test case 2: Non-empty DataFrame
    df = pd.DataFrame({'Age': [10, 20, 30], 'Weight': [50, 60, 70]})
    age = 15
    weight = 40
    expected_result = pd.DataFrame({'Age': [10, 20], 'Weight': [50, 60]})
    assert task_func(df, age, weight).equals(expected_result)

    # Test case 3: Standardization
    df = pd.DataFrame({'Age': [10, 20, 30], 'Weight': [50, 60, 70]})
    age = 15
    weight = 40
    expected_result = pd.DataFrame({'Age': [0, 1, 2], 'Weight': [0, 1, 2]})
    assert task_func(df, age, weight).equals(expected_result)