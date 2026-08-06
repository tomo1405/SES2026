python
import pytest
from src_0610 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    tuples = [('A', 'B'), ('C', 'D')]
    n_plots = 2
    
    expected_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'D': [10, 11, 12], 'E': [13, 14, 15]})
    expected_df = expected_df.set_index(['A', 'B', 'C', 'D', 'E']).drop(tuples, errors='ignore').reset_index()
    expected_plots = []
    possible_combinations = list(combinations(['A', 'B', 'C', 'D', 'E'], 2))
    for _ in range(min(n_plots, len(possible_combinations))):
        selected_columns = sample(possible_combinations, 1)[0]
        possible_combinations.remove(selected_columns)
        ax = expected_df.plot.scatter(x=selected_columns[0], y=selected_columns[1])
        expected_plots.append((selected_columns, ax))
    
    result_df, result_plots = task_func(df, tuples, n_plots)
    
    assert_frame_equal(result_df, expected_df)
    assert len(result_plots) == len(expected_plots)
    for i in range(len(result_plots)):
        assert result_plots[i][0] == expected_plots[i][0]
        assert_frame_equal(result_plots[i][1].get_lines()[0].get_data(), expected_plots[i][1].get_lines()[0].get_data())