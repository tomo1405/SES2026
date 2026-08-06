python
import pandas as pd
import pytest
from src_1018 import task_func

def test_task_func():
    # Test case 1: Valid input file, valid target column, default test size and n_estimators
    csv_file_path = "data/test_data.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100
    expected_report = """precision    recall  f1-score   support

           0       0.90      0.90      0.90        10
           1       0.90      0.90      0.90        10
           2       0.90      0.90      0.90        10

    accuracy                           0.90        30
   macro avg       0.90      0.90      0.90        30
weighted avg       0.90      0.90      0.90        30"""
    report = task_func(csv_file_path, target_column, test_size, n_estimators)
    assert report == expected_report

    # Test case 2: Valid input file, valid target column, custom test size and n_estimators
    csv_file_path = "data/test_data.csv"
    target_column = "target"
    test_size = 0.3
    n_estimators = 50
    expected_report = """precision    recall  f1-score   support

           0       0.90      0.90      0.90        10
           1       0.90      0.90      0.90        10
           2       0.90      0.90      0.90        10

    accuracy                           0.90        30
   macro avg       0.90      0.90      0.90        30
weighted avg       0.90      0.90      0.90        30"""
    report = task_func(csv_file_path, target_column, test_size, n_estimators)
    assert report == expected_report

    # Test case 3: Valid input file, invalid target column, default test size and n_estimators
    csv_file_path = "data/test_data.csv"
    target_column = "invalid_target"
    test_size = 0.2
    n_estimators = 100
    with pytest.raises(ValueError):
        report = task_func(csv_file_path, target_column, test_size, n_estimators)

    # Test case 4: Invalid input file, valid target column, default test size and n_estimators
    csv_file_path = "invalid_file.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100
    with pytest.raises(FileNotFoundError):
        report = task_func(csv_file_path, target_column, test_size, n_estimators)