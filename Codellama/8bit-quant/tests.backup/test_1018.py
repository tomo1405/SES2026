import pytest
from src_1018 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100

    report = task_func(csv_file_path, target_column, test_size, n_estimators)

    assert isinstance(report, str)
    assert len(report.split("\n")) == 11
    assert report.startswith("Classification Report")
    assert report.endswith("Overall Accuracy: 0.8")