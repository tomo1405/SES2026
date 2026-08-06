import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
from unittest.mock import patch, call, MagicMock
from src_1054 import task_func

def test_task_func_with_save_path():
    file_path = "test.csv"
    save_path = "test.png"
    with patch("matplotlib.pyplot.savefig") as mock_savefig:
        task_func(file_path, save_path)
        mock_savefig.assert_called_once_with(save_path)

def test_task_func_without_save_path():
    file_path = "test.csv"
    with patch("matplotlib.pyplot.show") as mock_show:
        task_func(file_path)
        mock_show.assert_called_once()

def test_task_func_with_file_not_found():
    file_path = "test.csv"
    save_path = "test.png"
    with patch("pandas.read_csv", side_effect=FileNotFoundError("File not found")):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            with patch("sys.exit") as mock_exit:
                task_func(file_path, save_path)
                mock_savefig.assert_not_called()
                mock_exit.assert_called_once_with(1)

def test_task_func_with_other_exception():
    file_path = "test.csv"
    save_path = "test.png"
    with patch("pandas.read_csv", side_effect=Exception("An error occurred")):
        with patch("matplotlib.pyplot.savefig") as mock_savefig:
            with patch("sys.exit") as mock_exit:
                task_func(file_path, save_path)
                mock_savefig.assert_not_called()
                mock_exit.assert_not_called()