python
import numpy as np
import pytest
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(n_samples=100, n_features=10, random_seed=None):
    # Generate synthetic data
    X, y = datasets.make_regression(
        n_samples=n_samples, n_features=n_features, noise=0.1, random_state=random_seed
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_seed
    )

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)
    coefficients = model.coef_
    intercept = model.intercept_

    mse = np.mean((predictions - y_test) ** 2)
    return predictions, coefficients, intercept, mse

def test_task_func():
    # Test case 1: default parameters
    predictions, coefficients, intercept, mse = task_func()
    assert len(predictions) == 20
    assert len(coefficients) == 10
    assert len(intercept) == 1
    assert mse > 0

    # Test case 2: custom parameters
    predictions, coefficients, intercept, mse = task_func(n_samples=50, n_features=5, random_seed=42)
    assert len(predictions) == 10
    assert len(coefficients) == 5
    assert len(intercept) == 1
    assert mse > 0

    # Test case 3: invalid parameters
    with pytest.raises(ValueError):
        task_func(n_samples=-10)
    with pytest.raises(ValueError):
        task_func(n_features=-5)
    with pytest.raises(ValueError):
        task_func(random_seed="invalid")