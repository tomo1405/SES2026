import pytest
from src_0453 import task_func

def test_task_func():
    # Test that the function returns the correct number of predictions
    predictions, coefficients, intercept, mse = task_func()
    assert len(predictions) == 100

    # Test that the function returns the correct number of coefficients
    assert len(coefficients) == 10

    # Test that the function returns the correct intercept
    assert intercept == 0

    # Test that the function returns the correct MSE
    assert mse == 0.1

if __name__ == "__main__":
    pytest.main()