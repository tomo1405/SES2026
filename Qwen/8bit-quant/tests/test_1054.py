import os

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_1054 import task_func


# Mocking dependencies
class MockDataFrame:
    def __init__(self, data):
        self.data = data

    def read_csv(self, file_path, usecols, names, header):
        return pd.DataFrame(self.data, columns=names)

    def dropna(self):
        return self.data.dropna()

    def fit_transform(self, data):
        return self.data

    def vocabulary_(self):
        return {"word1": 0, "word2": 1}

    def sum(self, axis):
        return self.data.sum(axis=axis)

def test_task_func_file_not_found(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', lambda *args, **kwargs: None)
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("non_existent_file.csv")
    assert str(excinfo.value) == "File not found: non_existent_file.csv"

def test_task_func_no_save_path(monkeypatch):
    mock_data = [["text1"], ["text2"]]
    monkeypatch.setattr(pd, 'read_csv', lambda *args, **kwargs: pd.DataFrame(mock_data, columns=["Text"]))
    monkeypatch.setattr(CountVectorizer, 'fit_transform', lambda *args, **kwargs: pd.DataFrame([[1, 2], [3, 4]]))
    result = task_func("existent_file.csv")
    assert isinstance(result, plt.AxesSubplot)

def test_task_func_with_save_path(monkeypatch, tmpdir):
    mock_data = [["text1"], ["text2"]]
    monkeypatch.setattr(pd, 'read_csv', lambda *args, **kwargs: pd.DataFrame(mock_data, columns=["Text"]))
    monkeypatch.setattr(CountVectorizer, 'fit_transform', lambda *args, **kwargs: pd.DataFrame([[1, 2], [3, 4]]))
    save_path = os.path.join(tmpdir, "output.png")
    task_func("existent_file.csv", save_path)
    assert os.path.exists(save_path)

def test_task_func_empty_file(monkeypatch):
    mock_data = []
    monkeypatch.setattr(pd, 'read_csv', lambda *args, **kwargs: pd.DataFrame(mock_data, columns=["Text"]))
    result = task_func("empty_file.csv")
    assert result is None