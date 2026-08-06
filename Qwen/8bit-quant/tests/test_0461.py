import subprocess
from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0461 import task_func


# Mock subprocess.run to avoid actual script execution
class MockCompletedProcess:
    returncode = 0

def mock_subprocess_run(*args, **kwargs):
    return MockCompletedProcess()

# Mock pandas read_csv to simulate CSV file reading
def mock_read_csv(file_path):
    if file_path == "valid_output.csv":
        data = StringIO("col1,col2\n1,2\n3,4")
    elif file_path == "invalid_columns.csv":
        data = StringIO("col1,col2,col3\n1,2,3\n4,5,6")
    else:
        raise FileNotFoundError
    return pd.read_csv(data)

@pytest.fixture(autouse=True)
def patch_subprocess_and_pandas(monkeypatch):
    monkeypatch.setattr(subprocess, 'run', mock_subprocess_run)
    monkeypatch.setattr(pd, 'read_csv', mock_read_csv)

def test_task_func_valid_script_and_output():
    script_path = "valid_script.py"
    output_file_path = "valid_output.csv"
    df, ax = task_func(script_path, output_file_path)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) == 2
    assert ax.get_xlabel() == "col1"
    plt.close(ax.figure)

def test_task_func_invalid_script():
    script_path = "non_existent_script.py"
    output_file_path = "valid_output.csv"
    with pytest.raises(ValueError, match="Error occurred while executing the script or script not found"):
        task_func(script_path, output_file_path)

def test_task_func_invalid_csv_columns():
    script_path = "valid_script.py"
    output_file_path = "invalid_columns.csv"
    with pytest.raises(ValueError, match="CSV file must contain exactly 2 columns"):
        task_func(script_path, output_file_path)