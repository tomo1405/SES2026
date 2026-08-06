import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
def task_func(data, target, test_size=0.2, random_state=None):
    data = pd.DataFrame(data)
    if data.empty or target not in data.columns:
        raise ValueError("Data must not be empty and target column must exist in the DataFrame.")

    # Splitting the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(columns=[target]), data[target], test_size=test_size, random_state=random_state
    )

    # Training the model
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)

    # Making predictions and returning the MSE
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse, model, data
import pytest
def test_task_func():
    data = [[1, 2], [3, 4], [5, 6]]
    target = 'target'
    test_size = 0.2
    random_state = 42
    with pytest.raises(ValueError) as excinfo:
        task_func(data, target, test_size, random_state)
    assert "Data must not be empty and target column must exist in the DataFrame." in str(excinfo.value)
    data = pd.DataFrame(data)
    data[target] = [1, 2, 3]
    mse, model, data = task_func(data, target, test_size, random_state)
    assert isinstance(mse, float)
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)