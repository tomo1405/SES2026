import pytest
from src_0482 import task_func

def test_task_func_with_empty_list():
    result = task_func([])
    assert result.empty
    assert list(result.columns) == ["Original String", "Randomized String"]

def test_task_func_with_single_element():
    data_list = ["apple, banana, cherry"]
    expected_df = pd.DataFrame({
        "Original String": ["apple, banana, cherry"],
        "Randomized String": ["banana, apple, cherry"]
    })
    result = task_func(data_list)
    assert result.equals(expected_df)

def test_task_func_with_multiple_elements():
    data_list = [
        "apple, banana, cherry",
        "dog, elephant, frog"
    ]
    expected_df = pd.DataFrame({
        "Original String": [
            "apple, banana, cherry",
            "dog, elephant, frog"
        ],
        "Randomized String": [
            "banana, apple, cherry",
            "elephant, frog, dog"
        ]
    })
    result = task_func(data_list)
    assert result.equals(expected_df)

def test_task_func_with_single_word_elements():
    data_list = [
        "apple",
        "banana",
        "cherry"
    ]
    expected_df = pd.DataFrame({
        "Original String": [
            "apple",
            "banana",
            "cherry"
        ],
        "Randomized String": [
            "apple",
            "banana",
            "cherry"
        ]
    })
    result = task_func(data_list)
    assert result.equals(expected_df)

def test_task_func_with_different_seed():
    data_list = ["apple, banana, cherry"]
    result1 = task_func(data_list, seed=1)
    result2 = task_func(data_list, seed=2)
    assert not result1.equals(result2)

def test_task_func_with_no_commas():
    data_list = ["apple banana cherry"]
    expected_df = pd.DataFrame({
        "Original String": ["apple banana cherry"],
        "Randomized String": ["apple banana cherry"]
    })
    result = task_func(data_list)
    assert result.equals(expected_df)