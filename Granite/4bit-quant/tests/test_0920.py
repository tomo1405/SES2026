from unittest.mock import patch

import pandas as pd


@patch('matplotlib.pyplot.show')
def test_task_func(mock_show):
    data = {'Category': ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'D', 'E']}
    df = pd.DataFrame(data)
    ax = task_func(df, 'Category')
    assert ax is not None
    mock_show.assert_called_once()