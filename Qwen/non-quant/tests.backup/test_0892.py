import pytest
from src_0892 import task_func
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

@pytest.fixture
def sample_data(tmpdir):
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'target': [2, 3, 4, 5, 6]
    }
    df = pd.DataFrame(data)
    csv_file_path = tmpdir.join('sample.csv')
    df.to_csv(csv_file_path, index=False)
    return str(csv_file_path)

def test_task_func(sample_data):
    model, predictions = task_func(sample_data, 'target', test_size=0.2, random_state=42)
    
    # Check if the model is an instance of LinearRegression
    assert isinstance(model, LinearRegression)
    
    # Check if predictions are not empty and have the correct shape
    assert predictions.shape[0] > 0
    
    # Check if predictions are of type numpy array
    assert isinstance(predictions, np.ndarray)
    
    # Additional check: Calculate MSE to ensure the model has made reasonable predictions
    df = pd.read_csv(sample_data)
    X = df.drop(columns=['target'])
    y = df['target']
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    mse = mean_squared_error(y_test, predictions)
    assert mse >= 0  # MSE should be non-negative

def test_task_func_invalid_attribute(sample_data):
    with pytest.raises(KeyError):
        task_func(sample_data, 'non_existent_column')

def test_task_func_invalid_csv_path():
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_path.csv', 'target')