import pytest
from src_1054 import task_func
import pandas as pd
import os
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data_file(tmpdir):
    data = {"Text": ["example text", "another example", "text with more words"]}
    df = pd.DataFrame(data)
    file_path = tmpdir.join("sample.csv")
    df.to_csv(file_path, index=False, header=False)
    return str(file_path)

def test_task_func_valid_file(sample_data_file, tmpdir):
    save_path = tmpdir.join("output.png")
    result = task_func(sample_data_file, save_path=str(save_path))
    assert os.path.exists(save_path)
    assert result is None

def test_task_func_invalid_file():
    with pytest.raises(FileNotFoundError) as exc_info:
        task_func("non_existent_file.csv")
    assert "File not found: non_existent_file.csv" in str(exc_info.value)

def test_task_func_no_save_path(sample_data_file):
    result = task_func(sample_data_file)
    assert isinstance(result, plt.Axes)

def test_task_func_empty_file(tmpdir):
    empty_file = tmpdir.join("empty.csv")
    empty_file.write("")
    with pytest.raises(Exception) as exc_info:
        task_func(str(empty_file))
    assert "An error occurred" in str(exc_info.value)