python
import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src_0879 import task_func

def test_task_func():
    # Test case 1: data is empty
    data = []
    target = 'target'
    with pytest.raises(ValueError):
        task_func(data, target)

    # Test case 2: target column does not exist in the DataFrame
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    target = 'target'
    with pytest.raises(ValueError):
        task_func(data, target)

    # Test case 3: test_size is not a float
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    with pytest.raises(TypeError):
        task_func(data, target, test_size='0.2')

    # Test case 4: test_size is negative
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    with pytest.raises(ValueError):
        task_func(data, target, test_size=-0.2)

    # Test case 5: test_size is greater than 1
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    with pytest.raises(ValueError):
        task_func(data, target, test_size=1.2)

    # Test case 6: random_state is not an integer
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    with pytest.raises(TypeError):
        task_func(data, target, random_state='123')

    # Test case 7: random_state is negative
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    with pytest.raises(ValueError):
        task_func(data, target, random_state=-123)

    # Test case 8: valid input
    data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'target': [7, 8, 9]})
    target = 'target'
    mse, model, data = task_func(data, target)
    assert isinstance(mse, float)
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)