import pytest
from src_0237 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
        'Age': [25, 30, 35, 40, 45, 25],
        'Score': [88, 92, 87, 94, 90, 88],
        'Category': ['A', 'B', 'A', 'B', 'A', 'A']
    }
    return pd.DataFrame(data)

def test_task_func_input_type(sample_df):
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_duplicate_removal(sample_df):
    df_with_duplicates = sample_df.copy()
    df_with_duplicates.loc[5, 'Age'] = 26  # Change age to make it a unique row
    result = task_func(df_with_duplicates)
    assert result == task_func(sample_df)

def test_task_func_accuracy(sample_df):
    accuracy = task_func(sample_df)
    assert 0 <= accuracy <= 1

def test_task_func_test_size(sample_df):
    accuracy_default = task_func(sample_df)
    accuracy_custom = task_func(sample_df, test_size=0.3)
    assert accuracy_default != accuracy_custom

def test_task_func_random_state(sample_df):
    accuracy_default = task_func(sample_df)
    accuracy_same_state = task_func(sample_df, random_state=42)
    assert accuracy_default == accuracy_same_state

    accuracy_different_state = task_func(sample_df, random_state=123)
    assert accuracy_default != accuracy_different_state