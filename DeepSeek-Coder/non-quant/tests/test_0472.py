import pytest
from src_0472 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    myList = ["apple", "banana", "apple", "banana", "orange"]
    result = task_func(myList)
    expected_df = pd.DataFrame({
        'apple': [2],
        'banana': [2],
        'orange': [1]
    })
    pd.testing.assert_frame_equal(result, expected_df)

    # Add more test cases as needed

# You can add more test cases to cover different scenarios