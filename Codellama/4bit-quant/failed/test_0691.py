import pytest
from src_0691 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]})

def test_task_func(df):
    model = task_func(df)
    assert isinstance(model, LinearRegression)
    assert model.coef_[0] == 1.0
    assert model.intercept_ == 0.0

def test_task_func_with_invalid_input(df):
    with pytest.raises(ValueError):
        task_func(df, 'invalid_input')