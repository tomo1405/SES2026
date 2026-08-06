import pytest
from src_0461 import task_func
import pandas as pd
import os

# Mocking subprocess and pandas for testing
class MockSubprocess:
    def run(self, args, check):
        if args[0] == "non_existent_script.py":
            raise FileNotFoundError("Mocked FileNotFoundError")
        elif args[0] == "error_script.py":
            raise subprocess.CalledProcessError(1, args)
        return True

class MockPandas:
    @staticmethod
    def read_csv(file_path):
        if file_path == "invalid_columns.csv":
            return pd.DataFrame(columns=["A", "B", "C"])
        elif file_path == "valid_data.csv":
            return pd.DataFrame({
                "Category": ["X", "Y", "Z"],
                "Value": [10, 20, 30]
            })
        else:
            raise FileNotFoundError("Mocked FileNotFoundError")

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'run', MockSubprocess().run)

@pytest.fixture
def mock_pandas(monkeypatch):
    monkeypatch.setattr(pd, 'read_csv', MockPandas.read_csv)

def test_task_func_success(mock_subprocess, mock_pandas, tmpdir):
    script_path = "valid_script.py"
    output_file_path = str(tmpdir.join("output.csv"))
    df = pd.DataFrame({
        "Category": ["X", "Y", "Z"],
        "Value": [10, 20, 30]
    })
    df.to_csv(output_file_path, index=False)

    result_df, ax = task_func(script_path, output_file_path)
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.equals(df)
    assert ax.get_xlabel() == "Category"

def test_task_func_non_existent_script(mock_subprocess, mock_pandas):
    with pytest.raises(ValueError, match="Error occurred while executing the script or script not found"):
        task_func("non_existent_script.py", "output.csv")

def test_task_func_error_script(mock_subprocess, mock_pandas):
    with pytest.raises(ValueError, match="Error occurred while executing the script or script not found"):
        task_func("error_script.py", "output.csv")

def test_task_func_invalid_columns(mock_subprocess, mock_pandas, tmpdir):
    script_path = "valid_script.py"
    output_file_path = str(tmpdir.join("invalid_columns.csv"))

    with pytest.raises(ValueError, match="CSV file must contain exactly 2 columns"):
        task_func(script_path, output_file_path)

def test_task_func_invalid_output_file(mock_subprocess, mock_pandas):
    with pytest.raises(FileNotFoundError):
        task_func("valid_script.py", "non_existent_output.csv")