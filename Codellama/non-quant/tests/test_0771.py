from src_0771 import task_func


def test_task_func():
    # Test that the function returns a tuple with two elements
    result = task_func()
    assert isinstance(result, tuple)
    assert len(result) == 2

    # Test that the first element of the tuple is a float
    r_squared, model = result
    assert isinstance(r_squared, float)

    # Test that the second element of the tuple is a LinearRegression object
    assert isinstance(model, LinearRegression)

    # Test that the LinearRegression object has a fit method
    assert hasattr(model, 'fit')

    # Test that the fit method returns a LinearRegression object
    assert isinstance(model.fit(X_train, y_train), LinearRegression)

    # Test that the LinearRegression object has a score method
    assert hasattr(model, 'score')

    # Test that the score method returns a float
    assert isinstance(model.score(X_test, y_test), float)

    # Test that the score method returns a value between 0 and 1
    assert 0 <= model.score(X_test, y_test) <= 1