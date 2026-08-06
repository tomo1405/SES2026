import pytest
from src_1018 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100

    # Test if the function raises an error if the target column is not found in the CSV file
    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column="invalid_target", test_size=test_size, n_estimators=n_estimators)

    # Test if the function returns the expected output for a valid CSV file
    expected_report = "precision    recall  f1-score   support\n\n0       0.89      0.94      0.92        7\n1       0.93      0.88      0.90        9\n\naccuracy                           0.91       16\nmacro avg       0.91      0.91      0.91       16\nweighted avg       0.91      0.91      0.91       16"
    actual_report = task_func(csv_file_path, target_column=target_column, test_size=test_size, n_estimators=n_estimators)
    assert actual_report == expected_report