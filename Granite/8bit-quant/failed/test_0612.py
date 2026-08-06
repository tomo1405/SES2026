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
    for columns in plot_details:
        assert len(columns) == 2
        assert columns[0] in COLUMNS
        assert columns[1] in COLUMNS