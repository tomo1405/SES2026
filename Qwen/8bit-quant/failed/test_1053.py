import pytest
from src_1053 import task_func
import pandas as pd
import os

@pytest.fixture
def sample_data_file(tmpdir):
    data = ["This is a test", "Another test line", "Yet another line"]
    file_path = tmpdir.join("sample.csv")
    df = pd.DataFrame(data, columns=["Text"])
    df.to_csv(file_path, index=False, header=False)
    return str(file_path)

def test_task_func_with_save_path(sample_data_file, tmpdir):
    save_path = str(tmpdir.join("output.png"))
    result = task_func(sample_data_file, save_path=save_path)
    assert result is None
    assert os.path.exists(save_path)

def test_task_func_without_save_path(sample_data_file):
    result = task_func(sample_data_file)
    assert isinstance(result, plt.AxesSubplot)

def test_task_func_empty_file(tmpdir):
    file_path = tmpdir.join("empty.csv")
    file_path.write("")
    result = task_func(str(file_path))
    assert result is None

def test_task_func_only_stop_words(tmpdir):
    data = ["a", "an", "the", "in", "on", "at", "and", "or"]
    file_path = tmpdir.join("stop_words.csv")
    df = pd.DataFrame(data, columns=["Text"])
    df.to_csv(file_path, index=False, header=False)
    result = task_func(str(file_path))
    assert result is None

def test_task_func_single_line(tmpdir):
    data = ["This is a test line with some words"]
    file_path = tmpdir.join("single_line.csv")
    df = pd.DataFrame(data, columns=["Text"])
    df.to_csv(file_path, index=False, header=False)
    result = task_func(str(file_path))
    assert isinstance(result, plt.AxesSubplot)