import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0612 import task_func


@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12],
        'D': [13, 14, 15, 16],
        'E': [17, 18, 19, 20]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_tuples():
    return [(1, 5), (3, 11)]

def test_task_func_output(sample_df, sample_tuples, monkeypatch):
    # Mock the plotting function to avoid actual plotting
    monkeypatch.setattr(plt, 'show', lambda: None)

    # Call the function with test data
    result_df, plot_details = task_func(sample_df, sample_tuples, 2)

    # Check that the correct rows are removed
    expected_df = sample_df[(sample_df['A'] != 1) | (sample_df['B'] != 5) | (sample_df['C'] != 3) | (sample_df['D'] != 11)]
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check that plot details are correctly generated
    assert len(plot_details) == min(2, len(result_df))
    for x_col, y_col in plot_details:
        assert x_col in COLUMNS
        assert y_col in COLUMNS
        assert x_col != y_col

def test_task_func_no_rows_removed(sample_df, sample_tuples, monkeypatch):
    # Mock the plotting function to avoid actual plotting
    monkeypatch.setattr(plt, 'show', lambda: None)

    # Modify sample_tuples to not match any row in sample_df
    sample_tuples = [(0, 0), (0, 0)]

    # Call the function with test data
    result_df, plot_details = task_func(sample_df, sample_tuples, 2)

    # Check that no rows are removed
    pd.testing.assert_frame_equal(result_df, sample_df)

    # Check that plot details are correctly generated
    assert len(plot_details) == min(2, len(result_df))
    for x_col, y_col in plot_details:
        assert x_col in COLUMNS
        assert y_col in COLUMNS
        assert x_col != y_col

def test_task_func_zero_plots(sample_df, sample_tuples, monkeypatch):
    # Mock the plotting function to avoid actual plotting
    monkeypatch.setattr(plt, 'show', lambda: None)

    # Call the function with test data and zero plots
    result_df, plot_details = task_func(sample_df, sample_tuples, 0)

    # Check that no rows are removed
    pd.testing.assert_frame_equal(result_df, sample_df)

    # Check that no plot details are generated
    assert len(plot_details) == 0

def test_task_func_more_plots_than_rows(sample_df, sample_tuples, monkeypatch):
    # Mock the plotting function to avoid actual plotting
    monkeypatch.setattr(plt, 'show', lambda: None)

    # Call the function with test data and more plots than available rows
    result_df, plot_details = task_func(sample_df, sample_tuples, 10)

    # Check that no rows are removed
    pd.testing.assert_frame_equal(result_df, sample_df)

    # Check that plot details are correctly generated based on available rows
    assert len(plot_details) == len(result_df)
    for x_col, y_col in plot_details:
        assert x_col in COLUMNS
        assert y_col in COLUMNS
        assert x_col != y_col