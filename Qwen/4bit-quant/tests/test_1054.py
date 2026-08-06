import pytest
from src_1054 import task_func
import pandas as pd
import os
import matplotlib.pyplot as plt

@pytest.fixture
def create_test_csv(tmp_path):
    test_data = {
        "Text": [
            "This is a test sentence.",
            "Another example sentence for testing.",
            "Yet another sentence for testing purposes."
        ]
    }
    test_df = pd.DataFrame(test_data)
    test_file_path = tmp_path / "test.csv"
    test_df.to_csv(test_file_path, index=False)
    return test_file_path

def test_task_func(create_test_csv, tmp_path):
    test_file_path = create_test_csv
    save_path = tmp_path / "test_plot.png"

    # Test when save_path is provided
    task_func(str(test_file_path), str(save_path))
    assert save_path.exists(), "The plot was not saved to the specified path."

    # Test when save_path is not provided
    ax = task_func(str(test_file_path))
    assert isinstance(ax, plt.Axes), "The function did not return a matplotlib Axes object."

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError, match="File not found"):
        task_func("non_existent_file.csv")

def test_task_func_empty_file(tmp_path):
    empty_file_path = tmp_path / "empty.csv"
    empty_file_path.touch()

    with pytest.warns(UserWarning, match="An error occurred"):
        result = task_func(str(empty_file_path))
        assert result is None, "The function should return None for an empty file."