import pytest
from src_1018 import task_func
import pandas as pd
import os

@pytest.fixture
def sample_csv(tmpdir):
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [0, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    csv_file_path = tmpdir.join("sample.csv")
    df.to_csv(csv_file_path, index=False)
    return str(csv_file_path)

def test_task_func(sample_csv):
    report = task_func(sample_csv)
    assert isinstance(report, str)
    assert "precision" in report
    assert "recall" in report
    assert "f1-score" in report
    assert "support" in report

def test_task_func_missing_target_column(tmpdir):
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    csv_file_path = tmpdir.join("missing_target.csv")
    df.to_csv(csv_file_path, index=False)
    with pytest.raises(ValueError, match="'target' column not found in the CSV file."):
        task_func(str(csv_file_path))

def test_task_func_custom_parameters(sample_csv):
    report = task_func(sample_csv, target_column='target', test_size=0.3, n_estimators=50)
    assert isinstance(report, str)
    assert "precision" in report
    assert "recall" in report
    assert "f1-score" in report
    assert "support" in report

def test_task_func_empty_file(tmpdir):
    csv_file_path = tmpdir.join("empty.csv")
    open(csv_file_path, 'a').close()  # Create an empty file
    with pytest.raises(pd.errors.EmptyDataError):
        task_func(str(csv_file_path))