python
import pandas as pd
import pytest
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def task_func(csv_file_path, attribute, test_size=0.2, random_state=42):
    df = pd.read_csv(csv_file_path)
    X = df.drop(columns=[attribute])
    y = df[attribute]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    return model, predictions

def test_task_func():
    # Test case 1: Test with valid input
    model, predictions = task_func('data.csv', 'target')
    assert isinstance(model, LinearRegression)
    assert isinstance(predictions, pd.Series)

    # Test case 2: Test with invalid input
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.csv', 'target')

    with pytest.raises(ValueError):
        task_func('data.csv', 'invalid_attribute')

    with pytest.raises(TypeError):
        task_func('data.csv', 'target', test_size='invalid_test_size')

    with pytest.raises(TypeError):
        task_func('data.csv', 'target', random_state='invalid_random_state')