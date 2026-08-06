import pandas as pd
import pytest
from src_0608 import task_func


# Fixtures
@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6],
        'D': [6, 5, 4, 3, 2],
        'E': [1, 1, 1, 1, 1]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_tuples():
    return [(1, 5), (2, 4)]

@pytest.fixture
def sample_n_plots():
    return 2

# Tests
def test_task_func_removes_tuples(sample_df, sample_tuples, sample_n_plots):
    df, plots = task_func(sample_df.copy(), sample_tuples, sample_n_plots)
    assert df.equals(pd.DataFrame({
        'A': [3, 5],
        'B': [3, 1],
        'C': [4, 6],
        'D': [5, 2],
        'E': [1, 1]
    }))

def test_task_func_generates_correct_number_of_plots(sample_df, sample_tuples, sample_n_plots):
    df, plots = task_func(sample_df.copy(), sample_tuples, sample_n_plots)
    assert len(plots) == sample_n_plots

def test_task_func_plots_have_correct_columns(sample_df, sample_tuples, sample_n_plots):
    df, plots = task_func(sample_df.copy(), sample_tuples, sample_n_plots)
    for ax in plots:
        assert ax.get_xlabel() in COLUMNS
        assert ax.get_ylabel() in COLUMNS

def test_task_func_handles_no_tuples(sample_df, sample_n_plots):
    df, plots = task_func(sample_df.copy(), [], sample_n_plots)
    assert df.equals(sample_df)

def test_task_func_handles_no_plots(sample_df, sample_tuples):
    df, plots = task_func(sample_df.copy(), sample_tuples, 0)
    assert len(plots) == 0

def test_task_func_handles_empty_dataframe(sample_df, sample_tuples, sample_n_plots):
    empty_df = pd.DataFrame(columns=COLUMNS)
    df, plots = task_func(empty_df.copy(), sample_tuples, sample_n_plots)
    assert df.empty
    assert len(plots) == sample_n_plots

def test_task_func_handles_duplicate_tuples(sample_df, sample_tuples, sample_n_plots):
    df, plots = task_func(sample_df.copy(), sample_tuples * 2, sample_n_plots)
    assert df.equals(pd.DataFrame({
        'A': [3, 5],
        'B': [3, 1],
        'C': [4, 6],
        'D': [5, 2],
        'E': [1, 1]
    }))