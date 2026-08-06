import pytest
from src_0890 import task_func
import pandas as pd
import numpy as np
import os

# Mocking os.path.join to control file paths
def mock_os_path_join(data_dir, csv_file):
    return f"{data_dir}/{csv_file}"

os.path.join = mock_os_path_join

# Mocking pd.read_csv to simulate different scenarios
def mock_pd_read_csv(file_path):
    if "empty.csv" in file_path:
        raise pd.errors.EmptyDataError("No data")
    elif "numeric.csv" in file_path:
        return pd.DataFrame({
            'A': [1, 2, np.nan, 4],
            'B': [5, np.nan, np.nan, 8]
        })
    elif "no_numeric.csv" in file_path:
        return pd.DataFrame({
            'A': ['a', 'b', 'c'],
            'B': ['d', 'e', 'f']
        })
    else:
        return pd.DataFrame()

pd.read_csv = mock_pd_read_csv

def test_task_func_empty_file(tmpdir):
    data_dir = tmpdir.mkdir("data")
    empty_file = data_dir.join("empty.csv")
    empty_file.write("")
    
    result = task_func(str(data_dir), "empty.csv")
    assert result.empty

def test_task_func_numeric_data(tmpdir):
    data_dir = tmpdir.mkdir("data")
    numeric_file = data_dir.join("numeric.csv")
    numeric_file.write("A,B\n1,5\n2,\n,7\n4,8")
    
    result = task_func(str(data_dir), "numeric.csv")
    expected_mean_A = (1 + 2 + 4) / 3
    expected_mean_B = (5 + 7 + 8) / 3
    assert result['A'].isnull().sum() == 0
    assert result['B'].isnull().sum() == 0
    assert result['A'].iloc[2] == expected_mean_A
    assert result['B'].iloc[1] == expected_mean_B

def test_task_func_no_numeric_data(tmpdir):
    data_dir = tmpdir.mkdir("data")
    no_numeric_file = data_dir.join("no_numeric.csv")
    no_numeric_file.write("A,B\na,d\ne,f\nc,g")
    
    result = task_func(str(data_dir), "no_numeric.csv")
    assert result.equals(pd.DataFrame({
        'A': ['a', 'e', 'c'],
        'B': ['d', 'f', 'g']
    }))

def test_task_func_nonexistent_file(tmpdir):
    data_dir = tmpdir.mkdir("data")
    with pytest.raises(FileNotFoundError):
        task_func(str(data_dir), "nonexistent.csv")