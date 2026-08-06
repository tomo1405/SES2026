import pytest
from src_0572 import task_func
import pandas as pd

def test_valid_input():
    f_list = [print, len, sum]
    file_path = "test_file.csv"
    task_func(f_list, file_path)
    df = pd.read_csv(file_path)
    assert df.shape == (3, 5)
    assert df['Function Name'].tolist() == ['print', 'len', 'sum']
    assert df['Number of Arguments'].tolist() == [0, 1, 1]
    assert df['Defaults'].tolist() == [None, None, None]
    assert df['Annotations'].tolist() == [None, None, None]
    assert df['Is Lambda'].tolist() == [False, False, False]

def test_invalid_f_list():
    f_list = [1, 2, 3]
    file_path = "test_file.csv"
    with pytest.raises(ValueError) as e:
        task_func(f_list, file_path)
    assert str(e.value) == "All elements in f_list must be callable functions."

def test_empty_f_list():
    f_list = []
    file_path = "test_file.csv"
    with pytest.raises(ValueError) as e:
        task_func(f_list, file_path)
    assert str(e.value) == "f_list should not be empty."

def test_invalid_file_path():
    f_list = [print, len, sum]
    file_path = 123
    with pytest.raises(IOError) as e:
        task_func(f_list, file_path)
    assert str(e.value) == "Error writing to file: must be str, not int"