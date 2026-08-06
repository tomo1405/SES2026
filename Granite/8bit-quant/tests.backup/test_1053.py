import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from unittest.mock import patch

from src_1053 import task_func

def test_task_func_with_valid_input():
    file_path = "path/to/file.csv"
    save_path = "path/to/save/plot.png"
    with patch("matplotlib.pyplot.savefig") as mock_savefig:
        ax = task_func(file_path, save_path)
        mock_savefig.assert_called_once_with(save_path)
        assert ax is None

def test_task_func_with_invalid_input():
    file_path = "path/to/file.csv"
    save_path = None
    df = pd.DataFrame({"Text": []})
    with patch("pandas.read_csv", return_value=df) as mock_read_csv:
        ax = task_func(file_path, save_path)
        mock_read_csv.assert_called_once_with(file_path, header=None, names=["Text"])
        assert ax is None

def test_task_func_with_no_valid_words():
    file_path = "path/to/file.csv"
    save_path = "path/to/save/plot.png"
    df = pd.DataFrame({"Text": ["a" * 100] * 10})
    with patch("pandas.read_csv", return_value=df) as mock_read_csv, patch(
        "sklearn.feature_extraction.text.CountVectorizer.fit_transform"
    ) as mock_fit_transform, patch("matplotlib.pyplot.bar") as mock_bar:
        mock_fit_transform.side_effect = ValueError("No valid words to plot.")
        ax = task_func(file_path, save_path)
        mock_read_csv.assert_called_once_with(file_path, header=None, names=["Text"])
        mock_fit_transform.assert_called_once()
        mock_bar.assert_not_called()
        assert ax is None