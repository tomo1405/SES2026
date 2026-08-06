python
import numpy as np
import pytest
from src_0453 import task_func

@pytest.fixture
def synthetic_data():
    X, y = datasets.make_regression(n_samples=100, n_features=10, noise=0.1, random_state=42)
    return X, y

def test_task_func(synthetic_data):
    X, y = synthetic_data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    coefficients = model.coef_
    intercept = model.intercept_

    mse = np.mean((predictions - y_test) ** 2)

    assert len(predictions) == len(y_test)
    assert len(coefficients) == X.shape[1]
    assert len(intercept) == 1
    assert mse > 0