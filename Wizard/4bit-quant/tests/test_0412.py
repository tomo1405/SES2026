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
    output_path = "test_data_output.json"
    result = task_func(data, output_path)
    assert result == output_path
    # Test case 2: Test with invalid input data (missing 'c' column)
    data = {"a": [1, 2, 3], "b": [4, 5, 6]}
    output_path = "test_data_output.json"
    result = task_func(data, output_path)
    assert result == output_path
    # Test case 3: Test with invalid input data (empty dictionary)
    data = {}
    output_path = "test_data_output.json"
    result = task_func(data, output_path)
    assert result == output_path