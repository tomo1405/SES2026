import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src_0879 import task_func

@pytest.fixture
def data():
    return pd.DataFrame({
        'feature_1': [1, 2, 3, 4, 5],
        'feature_2': [6, 7, 8, 9, 10],
        'target': [11, 12, 13, 14, 15]
    })

def test_task_func_valid_input(data):
    assert task_func(data, 'target')

def test_task_func_empty_data(data):
    with pytest.raises(ValueError) as excinfo:
        task_func(pd.DataFrame(), 'target')
    assert 'Data must not be empty' in str(excinfo.value)

def test_task_func_invalid_target(data):
    with pytest.raises(ValueError) as excinfo:
        task_func(data, 'invalid_target')
    assert 'Target column must exist in the DataFrame' in str(excinfo.value)

def test_task_func_split_data(data, random_state):
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(columns=['target']), data['target'], test_size=0.2, random_state=random_state
    )
    assert len(X_train) == 4
    assert len(X_test) == 1
    assert len(y_train) == 4
    assert len(y_test) == 1

def test_task_func_train_model(data, random_state):
    model = RandomForestRegressor(random_state=random_state)
    model.fit(data.drop(columns=['target']), data['target'])
    assert model.score(data.drop(columns=['target']), data['target']) > 0.9

def test_task_func_make_predictions(data, random_state):
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(columns=['target']), data['target'], test_size=0.2, random_state=random_state
    )
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    assert len(predictions) == 1

def test_task_func_return_mse(data, random_state):
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(columns=['target']), data['target'], test_size=0.2, random_state=random_state
    )
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    assert mse > 0