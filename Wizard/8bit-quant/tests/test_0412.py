python
import pandas as pd
import json
import pytest

def task_func(data: dict, output_path: str = "./default_data_output.json") -> str:
    df = pd.DataFrame(data)
    # Drop column named 'c' if it exists
    df = df.drop(columns="c", errors="ignore")
    # Convert the DataFrame to dictionary
    data_dict = df.to_dict(orient="dict")
    # Save the dictionary as a JSON file
    with open(output_path, "w") as file:
        json.dump(data_dict, file)

    return output_path

def test_task_func():
    # Test case 1: Test with valid input data
    data = {"a": [1, 2, 3], "b": [4, 5, 6]}
    output_path = "./test_data_output.json"
    expected_output_path = output_path
    assert task_func(data, output_path) == expected_output_path

    # Test case 2: Test with invalid input data (missing 'a' column)
    data = {"b": [4, 5, 6]}
    output_path = "./test_data_output.json"
    expected_output_path = output_path
    assert task_func(data, output_path) == expected_output_path

    # Test case 3: Test with invalid input data (missing 'b' column)
    data = {"a": [1, 2, 3]}
    output_path = "./test_data_output.json"
    expected_output_path = output_path
    assert task_func(data, output_path) == expected_output_path

    # Test case 4: Test with invalid input data (missing 'a' and 'b' columns)
    data = {}
    output_path = "./test_data_output.json"
    expected_output_path = output_path
    assert task_func(data, output_path) == expected_output_path

    # Test case 5: Test with invalid input data (invalid data type)
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": "invalid"}
    output_path = "./test_data_output.json"
    expected_output_path = output_path
    assert task_func(data, output_path) == expected_output_path

    # Test case 6: Test with invalid input data (invalid output path)
    data = {"a": [1, 2, 3], "b": [4, 5, 6]}
    output_path = "/invalid/path/test_data_output.json"
    expected_output_path = output_path
    with pytest.raises(FileNotFoundError):
        task_func(data, output_path)