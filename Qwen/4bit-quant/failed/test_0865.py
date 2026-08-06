import pytest
from src_0865 import task_func

def test_task_func_empty_input():
    result = task_func([])
    assert result.empty, "Should return an empty DataFrame for empty input"

def test_task_func_single_fruit():
    fruit_data = [('apple', 10)]
    expected_df = pd.DataFrame({'Total Count': [10], 'Average Count': [10]}, index=['apple'])
    result = task_func(fruit_data)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_multiple_fruits():
    fruit_data = [('apple', 10), ('banana', 20), ('apple', 30)]
    expected_df = pd.DataFrame({'Total Count': [40, 20], 'Average Count': [20, 20]}, index=['apple', 'banana'])
    result = task_func(fruit_data)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_duplicate_fruits():
    fruit_data = [('apple', 10), ('apple', 20), ('apple', 30)]
    expected_df = pd.DataFrame({'Total Count': [60], 'Average Count': [20]}, index=['apple'])
    result = task_func(fruit_data)
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_mixed_fruits():
    fruit_data = [('apple', 10), ('banana', 20), ('cherry', 30), ('banana', 40)]
    expected_df = pd.DataFrame({'Total Count': [10, 60, 30], 'Average Count': [10, 30, 30]}, index=['apple', 'banana', 'cherry'])
    result = task_func(fruit_data)
    pd.testing.assert_frame_equal(result, expected_df)