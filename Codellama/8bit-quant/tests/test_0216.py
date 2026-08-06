import pytest
from src_0216 import task_func

def test_task_func():
    url = 'https://api.example.com/data'
    parameters = {'param1': 'value1', 'param2': 'value2'}
    df, ax = task_func(url, parameters)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.heatmap)
    assert df.shape == (10, 10)
    assert ax.shape == (10, 10)
    assert ax.get_xlabel() == 'X'
    assert ax.get_ylabel() == 'Y'
    assert ax.get_title() == 'Correlation Heatmap'