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
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'D'], larger=5, equal=11)

def test_task_func_invalid_input_larger(df):
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'C'], larger=100, equal=11)

def test_task_func_invalid_input_equal(df):
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'C'], larger=5, equal=100)

def test_task_func_empty_contingency_table(df):
    with pytest.raises(ValueError):
        task_func(df, columns=['A', 'B', 'D'], larger=5, equal=11)

def test_task_func_chi_square_test(df):
    p_value = task_func(df, columns=['A', 'B', 'C'], larger=5, equal=11)
    contingency_table = pd.crosstab(df['A'], df['B'])
    _, p_value_expected, _, _ = chi2_contingency(contingency_table)
    assert p_value == p_value_expected