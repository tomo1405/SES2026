import pytest
from src_0112 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Time': ['12:00', '13:00', '14:00'],
                      'Temperature': [20, 22, 24]})
    ax = task_func(df)
    assert isinstance(ax, sns.heatmap)
    assert ax.get_title() == 'Temperature Heatmap'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Time': ['12:00', '13:00', '14:00'],
                      'Temperature': [20, 22, 24]})
    with pytest.raises(ValueError):
        task_func(df)