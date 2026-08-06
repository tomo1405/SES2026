import os
import re
import pandas as pd
import pytest
from src_0642 import task_func

@pytest.fixture
def setup():
    pattern = r".*\.csv$"
    directory = "test_directory"
    output_csv = "output.csv"
    return pattern, directory, output_csv

def test_task_func_with_valid_input(setup):
    pattern, directory, output_csv = setup
    df = task_func(pattern, directory, output_csv)
    assert isinstance(df, pd.DataFrame)
    assert os.path.exists(output_csv)

def test_task_func_with_invalid_pattern(setup):
    pattern, directory, output_csv = setup
    with pytest.raises(ValueError):
        task_func("invalid_pattern", directory, output_csv)

def test_task_func_with_nonexistent_directory(setup):
    pattern, directory, output_csv = setup
    with pytest.raises(FileNotFoundError):
        task_func(pattern, "nonexistent_directory", output_csv)

def test_task_func_with_invalid_output_csv(setup):
    pattern, directory, output_csv = setup
    with pytest.raises(IOError):
        task_func(pattern, directory, "invalid_output.txt")