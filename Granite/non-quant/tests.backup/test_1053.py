import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from src_1053 import task_func
import pytest

def test_task_func_with_valid_input():
    file_path = "path/to/valid/file.csv"
    save_path = "path/to/save/plot.png"
    ax = task_func(file_path, save_path)
    assert ax is not None

def test_task_func_with_invalid_input():
    file_path = "path/to/invalid/file.csv"
    save_path = None
    with pytest.raises(ValueError):
        task_func(file_path, save_path)

def test_task_func_with_empty_dataframe():
    file_path = "path/to/empty/file.csv"
    save_path = "path/to/save/plot.png"
    df = pd.DataFrame({"Text": []})
    df.to_csv(file_path, index=False)
    ax = task_func(file_path, save_path)
    assert ax is None

def test_task_func_with_only_stop_words():
    file_path = "path/to/only_stop_words.csv"
    save_path = "path/to/save/plot.png"
    df = pd.DataFrame({"Text": ["a a a a a a"]})
    df.to_csv(file_path, index=False)
    ax = task_func(file_path, save_path)
    assert ax is None