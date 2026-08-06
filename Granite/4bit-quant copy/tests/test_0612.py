import pytest
from src_0612 import task_func

@pytest.mark.parametrize("df, tuples, n_plots, expected_df_shape, expected_plot_details", [
    (
        # Test case 1: Test with empty dataframe and tuples
        pd.DataFrame(),
        [(1, 2), (3, 4)],
        2,
        (0, 5),
        []
    ),
    (
        # Test case 2: Test with non-empty dataframe and tuples
        pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9],
            'D': [10, 11, 12],
            'E': [13, 14, 15]
        }),
        [(1, 2), (3, 4)],
        2,
        (1, 5),
        [('A', 'B'), ('A', 'C')]
    ),
    (
        # Test case 3: Test with non-empty dataframe, tuples, and n_plots greater than dataframe size
        pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9],
            'D': [10, 11, 12],
            'E': [13, 14, 15]
        }),
        [(1, 2), (3, 4)],
        5,
        (1, 5),
        [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C')]
    )
])
def test_task_func(df, tuples, n_plots, expected_df_shape, expected_plot_details):
    df, plot_details = task_func(df, tuples, n_plots)
    assert df.shape == expected_df_shape
    assert plot_details == expected_plot_details