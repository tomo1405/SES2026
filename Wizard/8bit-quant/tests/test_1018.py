python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from src_1018 import task_func

def test_task_func():
    # Test case 1: Valid input
    csv_file_path = "data.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = 100
    expected_report = "precision    recall  f1-score   support\n" \
                      "\n" \
                      "       0       0.00      0.00      0.00         0\n" \
                      "       1       0.00      0.00      0.00         0\n" \
                      "\n" \
                      "    accuracy                           0.00         0\n" \
                      "   macro avg       0.00      0.00      0.00         0\n" \
                      "weighted avg       0.00      0.00      0.00         0\n"

    report = task_func(csv_file_path, target_column, test_size, n_estimators)
    assert report == expected_report

    # Test case 2: Invalid target column
    csv_file_path = "data.csv"
    target_column = "invalid_target"
    test_size = 0.2
    n_estimators = 100
    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column, test_size, n_estimators)

    # Test case 3: Invalid test size
    csv_file_path = "data.csv"
    target_column = "target"
    test_size = 1.2
    n_estimators = 100
    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column, test_size, n_estimators)

    # Test case 4: Invalid n_estimators
    csv_file_path = "data.csv"
    target_column = "target"
    test_size = 0.2
    n_estimators = -100
    with pytest.raises(ValueError):
        task_func(csv_file_path, target_column, test_size, n_estimators)