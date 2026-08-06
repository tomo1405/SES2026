import pandas as pd
import pytest
from scipy.stats import chi2_contingency
from src_0885 import task_func

@pytest.fixture
def df():
    return pd.DataFrame({
        'A': ['a', 'a', 'b', 'b', 'c', 'c'],
        'B': [1, 2, 3, 4, 5, 6],
        'C': [7, 8, 9, 10, 11, 12],
        'D': [13, 14, 15, 16, 17, 18]
    })

def test_task_func_valid_input(df):
    assert task_func(df, columns=['A', 'B', 'C'], larger=5, equal=11) is not None

def test_task_func_invalid_input_columns(df):
    with pytest.raises(ValueError) as excinfo:
        task_func(df, columns=['A', 'B'])
    assert 'Exactly three columns should be specified.' in str(excinfo.value)

def test_task_func_invalid_input_column_not_exists(df):
    with pytest.raises(ValueError) as excinfo:
        task_func(df, columns=['A', 'B', 'E'])
    assert 'The specified columns should exist in the DataFrame.' in str(excinfo.value)

def test_task_func_invalid_input_no_matching_data(df):
    with pytest.raises(ValueError) as excinfo:
        task_func(df, columns=['A', 'B', 'C'], larger=100, equal=11)
    assert 'Insufficient data - no matching data for the applied conditions.' in str(excinfo.value)

def test_task_func_expected_output(df):
    expected_p_value = chi2_contingency(pd.crosstab(df['A'], df['B']))[1]
    assert task_func(df, columns=['A', 'B', 'C']) == expected_p_value