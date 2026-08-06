import pandas as pd
import pytest
from src_0365 import task_func


def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(1)

def test_task_func_output_type():
    df = pd.DataFrame({'feature '+str(i): [i] for i in range(1, 11)})
    model = task_func(df)
    assert isinstance(model, LinearRegression)

def test_task_func_output_shape():
    df = pd.DataFrame({'feature '+str(i): [i] for i in range(1, 11)})
    model = task_func(df)
    assert model.coef_.shape == (10,)

def test_task_func_output_values():
    df = pd.DataFrame({'feature '+str(i): [i] for i in range(1, 11)})
    model = task_func(df)
    assert model.coef_[0] == 1
    assert model.coef_[1] == 2
    assert model.coef_[2] == 3
    assert model.coef_[3] == 4
    assert model.coef_[4] == 5
    assert model.coef_[5] == 6
    assert model.coef_[6] == 7
    assert model.coef_[7] == 8
    assert model.coef_[8] == 9
    assert model.coef_[9] == 10