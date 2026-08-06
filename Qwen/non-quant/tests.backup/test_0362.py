import pytest
from src_0362 import task_func
import pandas as pd
import os

# Mocking pandas read_excel and to_csv functions
class MockDataFrame:
    def __init__(self, data):
        self.data = data

    def sum(self, numeric_only=True):
        return pd.Series({col: sum(self.data[col]) for col in self.data.columns})

    def to_csv(self, path_or_buf, index=False):
        with open(path_or_buf, 'w') as f:
            f.write("col1,col2\n")
            for row in zip(*self.data.values()):
                f.write(f"{row[0]},{row[1]}\n")

def mock_read_excel(file_path, sheet_name=None):
    if file_path == "test.xlsx":
        return MockDataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    else:
        raise FileNotFoundError

def mock_to_csv(df, path_or_buf, index=False):
    pass

@pytest.fixture(autouse=True)
def patch_pandas(monkeypatch):
    monkeypatch.setattr(pd, 'read_excel', mock_read_excel)
    monkeypatch.setattr(MockDataFrame, 'to_csv', mock_to_csv)

def test_task_func_success(tmpdir):
    excel_file = tmpdir.join("test.xlsx")
    csv_file = tmpdir.join("test.csv")
    excel_file.write_binary(b"")

    result = task_func("Sheet1", str(excel_file), str(csv_file))
    assert result == {"col1": 6, "col2": 15}

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func("Sheet1", "non_existent.xlsx")
    assert str(excinfo.value) == "Excel file not found at non_existent.xlsx"

def test_task_func_invalid_sheet_name(tmpdir):
    excel_file = tmpdir.join("test.xlsx")
    excel_file.write_binary(b"")

    with pytest.raises(ValueError) as excinfo:
        task_func("InvalidSheet", str(excel_file))
    assert str(excinfo.value) == "Error in processing Excel file: No sheet named 'InvalidSheet'"