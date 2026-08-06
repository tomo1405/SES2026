import pytest
from src_0612 import task_func

def test_task_func():
    # Mock input data
    df = ...
    tuples = ...
    n_plots = ...

    # Call the function
    df, plot_details = task_func(df, tuples, n_plots)

    # Assert the output is as expected
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot_details, list)
    assert len(plot_details) == min(n_plots, len(df))
    for column_pair in plot_details:
        assert len(column_pair) == 2
        assert column_pair[0] in COLUMNS
        assert column_pair[1] in COLUMNS