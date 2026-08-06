import pytest
from src_0728 import task_func

def test_task_func():
    # Test case 1: input is a string
    input_str = "This is a sentence"
    expected_output = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert np.array_equal(task_func(input_str), expected_output)

    # Test case 2: input is a list of strings
    input_list = ["This is a sentence", "Another sentence here", "More sentences"]
    expected_output = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    assert np.array_equal(task_func(input_list), expected_output)

    # Test case 3: input is a numpy array
    input_array = np.array(["This is a sentence", "Another sentence here", "More sentences"])
    expected_output = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test case 4: input is a pandas dataframe
    input_df = pd.DataFrame({"sentence": ["This is a sentence", "Another sentence here", "More sentences"]})
    expected_output = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
    assert np.array_equal(task_func(input_df), expected_output)