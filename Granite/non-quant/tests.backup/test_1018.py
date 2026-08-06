import pytest
from src_1018 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100

    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column="invalid_column", test_size=test_size, n_estimators=n_estimators)

    report = task_func(csv_file_path, target_column=target_column, test_size=test_size, n_estimators=n_estimators)

    assert isinstance(report, str)
    assert "precision" in report
    assert "recall" in report
    assert "f1-score" in report
    assert "support" in report