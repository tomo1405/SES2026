import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from src_0365 import task_func
import pytest

# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'

def test_task_func_input():
    with pytest.raises(ValueError) as excinfo:
        task_func("not a DataFrame")
    assert "The input df is not a DataFrame" in str(excinfo.value)

def test_task_func_output():
    df = pd.DataFrame({
        FEATURES[0]: range(1, 11),
        FEATURES[1]: range(11, 21),
        TARGET: range(21, 31)
    })
    model = task_func(df)
    assert isinstance(model, LinearRegression)