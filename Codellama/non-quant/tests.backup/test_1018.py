import pytest
from src_1018 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100

    # Test with valid input
    report = task_func(csv_file_path, target_column, test_size, n_estimators)
    assert isinstance(report, str)
    assert len(report.split("\n")) == 11

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func("invalid_path.csv", target_column, test_size, n_estimators)

    with pytest.raises(ValueError):
        task_func(csv_file_path, "invalid_column", test_size, n_estimators)

    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column, -1, n_estimators)

    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column, test_size, -1)