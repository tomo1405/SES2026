import pytest
from src_0707 import task_func
import pandas as pd
from sklearn.datasets import make_classification

def test_task_func():
    # Create a sample dataset
    X, y = make_classification(n_samples=100, n_features=20, n_classes=2, random_state=42)
    columns = [f'feature_{i}' for i in range(20)]
    data = pd.DataFrame(X, columns=columns)
    data['target'] = y

    # Test with correct target column
    accuracy = task_func(data, columns, 'target')
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

    # Test with incorrect target column
    with pytest.raises(ValueError):
        task_func(data, columns, 'non_existent_column')

    # Test with empty dataframe
    empty_data = pd.DataFrame(columns=columns)
    with pytest.raises(ValueError):
        task_func(empty_data, columns, 'target')

    # Test with all zeros in target column
    data['target'] = 0
    accuracy = task_func(data, columns, 'target')
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1

    # Test with all ones in target column
    data['target'] = 1
    accuracy = task_func(data, columns, 'target')
    assert isinstance(accuracy, float)
    assert 0 <= accuracy <= 1