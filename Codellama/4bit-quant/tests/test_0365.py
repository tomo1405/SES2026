import pandas as pd
import pytest
from src_0365 import task_func


def test_task_func_input_type():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_output_type():
    df = pd.DataFrame(data={'feature '+str(i): [i] for i in range(1, 11)}, columns=['feature '+str(i) for i in range(1, 11)])
    model = task_func(df)
    assert isinstance(model, LinearRegression)

def test_task_func_output_shape():
    df = pd.DataFrame(data={'feature '+str(i): [i] for i in range(1, 11)}, columns=['feature '+str(i) for i in range(1, 11)])
    model = task_func(df)
    assert model.coef_.shape == (10,)
    assert model.intercept_.shape == (1,)

def test_task_func_output_values():
    df = pd.DataFrame(data={'feature '+str(i): [i] for i in range(1, 11)}, columns=['feature '+str(i) for i in range(1, 11)])
    model = task_func(df)
    assert model.coef_[0] == 1
    assert model.intercept_[0] == 0