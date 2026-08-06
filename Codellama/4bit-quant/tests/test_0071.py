import pytest
from src_0071 import task_func

def test_task_func():
    json_file = 'test_data.json'
    df, ax = task_func(json_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.columns.tolist() == COLUMNS + ['sum', 'mean']
    assert df['sum'].dtype == np.float64
    assert df['mean'].dtype == np.float64
    assert ax.get_xlabel() == 'sum'
    assert ax.get_ylabel() == 'mean'