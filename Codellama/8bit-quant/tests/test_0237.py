import pandas as pd
import pytest
from src_0237 import task_func


def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func(df=1, test_size=0.2, random_state=42)

def test_task_func_input_value():
    with pytest.raises(ValueError):
        task_func(df=pd.DataFrame(), test_size=0.2, random_state=42)

def test_task_func_output_type():
    assert isinstance(task_func(df=pd.DataFrame(), test_size=0.2, random_state=42), float)

def test_task_func_output_value():
    assert task_func(df=pd.DataFrame(), test_size=0.2, random_state=42) >= 0
    assert task_func(df=pd.DataFrame(), test_size=0.2, random_state=42) <= 1