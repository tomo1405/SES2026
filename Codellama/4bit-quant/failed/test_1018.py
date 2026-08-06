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
    assert len(report) > 0

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(csv_file_path, "invalid_column", test_size, n_estimators)

    # Test with different test size
    report = task_func(csv_file_path, target_column, 0.5, n_estimators)
    assert isinstance(report, str)
    assert len(report) > 0

    # Test with different number of estimators
    report = task_func(csv_file_path, target_column, test_size, 50)
    assert isinstance(report, str)
    assert len(report) > 0