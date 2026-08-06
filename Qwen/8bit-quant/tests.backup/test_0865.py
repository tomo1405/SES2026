import pytest
from src_0865 import task_func

def test_empty_input():
    result = task_func([])
    assert result.empty

def test_single_fruit():
    data = [('apple', 10)]
    expected_df = pd.DataFrame({'Total Count': [10], 'Average Count': [10]}, index=['apple'])
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_df)

def test_multiple_fruits():
    data = [('apple', 10), ('banana', 20), ('apple', 30)]
    expected_df = pd.DataFrame({'Total Count': [40, 20], 'Average Count': [20, 20]}, index=['apple', 'banana'])
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_df)

def test_duplicate_fruits():
    data = [('apple', 10), ('apple', 10), ('banana', 20)]
    expected_df = pd.DataFrame({'Total Count': [20, 20], 'Average Count': [10, 20]}, index=['apple', 'banana'])
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_df)

def test_mixed_case_fruits():
    data = [('Apple', 10), ('apple', 10), ('Banana', 20)]
    expected_df = pd.DataFrame({'Total Count': [20, 20], 'Average Count': [10, 20]}, index=['Apple', 'Banana'])
    result = task_func(data)
    pd.testing.assert_frame_equal(result, expected_df)