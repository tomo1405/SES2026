import pytest
from src_0303 import task_func
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_valid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    corr_df, heatmap = task_func(df, plot=True)
    assert isinstance(corr_df, pd.DataFrame)
    assert isinstance(heatmap, plt.Figure)

def test_task_func_invalid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

def test_task_func_invalid_input_2():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=True)

def test_task_func_invalid_input_3():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

def test_task_func_invalid_input_4():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=True)

def test_task_func_invalid_input_5():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

def test_task_func_invalid_input_6():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=True)

def test_task_func_invalid_input_7():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

def test_task_func_invalid_input_8():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=True)

def test_task_func_invalid_input_9():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

def test_task_func_invalid_input_10():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, plot=True)