import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from unittest.mock import patch

from src_0065 import task_func

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with patch('matplotlib.pyplot.show') as mock_show:
        analyzed_df, ax = task_func(data)
        mock_show.assert_called_once()
    assert isinstance(analyzed_df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.AxMesh)
    assert analyzed_df.columns.tolist() == COLUMNS[1:]
    assert analyzed_df.index.tolist() == [1, 4, 7]
    assert analyzed_df.loc[1, 'col2'] == 2
    assert ax.collections[0].get_paths()[0].vertices[:, 0].tolist() == [0.5, 1.5, 2.5, 3.5]