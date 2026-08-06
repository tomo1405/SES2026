import pytest
from src_0841 import task_func
import pandas as pd
import os

def test_task_func_output_file_exists(tmpdir):
    file_path = str(tmpdir / "test_output.csv")
    task_func(file_path, num_rows=10)
    assert os.path.exists(file_path)

def test_task_func_file_content(tmpdir):
    file_path = str(tmpdir / "test_output.csv")
    task_func(file_path, num_rows=5, data_dimensions=3, random_seed=42)
    df = pd.read_csv(file_path)
    assert df.shape == (5, 3)
    assert list(df.columns) == ['Feature_1', 'Feature_2', 'Feature_3']
    expected_data = pd.DataFrame({
        'Feature_1': [0.67063772, 0.41919477, 0.91337769, 0.55868984, 0.71518937],
        'Feature_2': [0.14675589, 0.78052918, 0.0202184 , 0.83261985, 0.26455481],
        'Feature_3': [0.41702200, 0.79172504, 0.52889492, 0.56804456, 0.49543509]
    })
    pd.testing.assert_frame_equal(df, expected_data)

def test_task_func_with_default_dimensions(tmpdir):
    file_path = str(tmpdir / "test_output.csv")
    task_func(file_path, num_rows=3)
    df = pd.read_csv(file_path)
    assert df.shape == (3, 5)
    assert list(df.columns) == ['Feature_1', 'Feature_2', 'Feature_3', 'Feature_4', 'Feature_5']

def test_task_func_with_random_seed(tmpdir):
    file_path = str(tmpdir / "test_output.csv")
    task_func(file_path, num_rows=2, data_dimensions=2, random_seed=0)
    df = pd.read_csv(file_path)
    expected_data = pd.DataFrame({
        'Feature_1': [0.54881350, 0.71518937],
        'Feature_2': [0.60276338, 0.54488318]
    })
    pd.testing.assert_frame_equal(df, expected_data)