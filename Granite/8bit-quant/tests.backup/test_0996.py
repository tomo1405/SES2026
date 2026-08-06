import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import patch, call
from src_0996 import task_func

def test_task_func_file_not_found():
    file_path = "path/to/file.csv"
    plot_path = "path/to/plot.png"
    with patch("os.path.isfile", return_value=False):
        with patch("pandas.read_csv") as mock_read_csv:
            with patch("matplotlib.pyplot.savefig") as mock_savefig:
                with patch("numpy.mean", return_value=np.nan) as mock_mean:
                    with patch("numpy.median", return_value=np.nan) as mock_median:
                        result = task_func(file_path, plot_path)
                        assert result == (np.nan, np.nan, plot_path)
                        mock_read_csv.assert_not_called()
                        mock_savefig.assert_not_called()
                        mock_mean.assert_not_called()
                        mock_median.assert_not_called()

def test_task_func_empty_file():
    file_path = "path/to/file.csv"
    plot_path = "path/to/plot.png"
    with patch("os.path.isfile", return_value=True):
        with patch("pandas.read_csv", side_effect=pd.errors.EmptyDataError):
            with patch("matplotlib.pyplot.savefig") as mock_savefig:
                with patch("numpy.mean", return_value=np.nan) as mock_mean:
                    with patch("numpy.median", return_value=np.nan) as mock_median:
                        result = task_func(file_path, plot_path)
                        assert result == (np.nan, np.nan, plot_path)
                        mock_savefig.assert_not_called()
                        mock_mean.assert_not_called()
                        mock_median.assert_not_called()

def test_task_func_valid_data():
    file_path = "path/to/file.csv"
    plot_path = "path/to/plot.png"
    data = pd.Series([1, 2, 3, 4, 5])
    with patch("os.path.isfile", return_value=True):
        with patch("pandas.read_csv", return_value=data):
            with patch("matplotlib.pyplot.savefig") as mock_savefig:
                with patch("numpy.mean", return_value=3) as mock_mean:
                    with patch("numpy.median", return_value=3) as mock_median:
                        result = task_func(file_path, plot_path)
                        assert result == (3.0, 3.0, plot_path)
                        mock_savefig.assert_called_once_with(plot_path)
                        mock_mean.assert_called_once_with(data)
                        mock_median.assert_called_once_with(data)