import pytest
from src_0480 import task_func

def test_task_func_with_empty_list():
    input_data = []
    expected_output = pd.DataFrame(columns=["Original String", "Modified String"])
    result = task_func(input_data)
    assert result.equals(expected_output)

def test_task_func_with_single_empty_string():
    input_data = ["   "]
    expected_output = pd.DataFrame({
        "Original String": ["   "],
        "Modified String": ["   "]
    })
    result = task_func(input_data)
    assert result.equals(expected_output)

def test_task_func_with_single_string_no_comma():
    input_data = ["hello"]
    expected_output = pd.DataFrame({
        "Original String": ["hello"],
        "Modified String": ["hello"]
    })
    result = task_func(input_data)
    assert result.equals(expected_output)

def test_task_func_with_single_string_with_comma():
    input_data = ["hello, world"]
    result = task_func(input_data)
    modified_string = result.iloc[0]["Modified String"]
    assert modified_string != "hello, world"
    assert modified_string.startswith("hello, ")
    assert len(modified_string.split(", ")[1]) == len("world")

def test_task_func_with_multiple_strings():
    input_data = ["apple, banana", "cherry, date", "elderberry, fig"]
    result = task_func(input_data)
    for i, original in enumerate(input_data):
        modified = result.iloc[i]["Modified String"]
        assert modified != original
        assert modified.count(", ") == 1
        substrings = modified.split(", ")
        assert len(substrings[0]) == len(original.split(", ")[0])
        assert len(substrings[1]) == len(original.split(", ")[1])

def test_task_func_with_seed():
    input_data = ["apple, banana", "cherry, date", "elderberry, fig"]
    seed_value = 42
    result_1 = task_func(input_data, seed=seed_value)
    result_2 = task_func(input_data, seed=seed_value)
    assert result_1.equals(result_2)