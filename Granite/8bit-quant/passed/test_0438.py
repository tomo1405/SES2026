import pickle
import os
import pytest
from src_0438 import task_func

def test_task_func():
    df = {"key": "value"}  # Replace this with your desired input data
    file_name = "save.pkl"
    expected_output = df

    # Test if the function returns the expected output
    assert task_func(df, file_name) == expected_output

    # Test if the file is created and removed correctly
    with open(file_name, "wb") as file:
        pickle.dump(df, file)

    with open(file_name, "rb") as file:
        loaded_df = pickle.load(file)

    os.remove(file_name)

    assert loaded_df == expected_output