import pytest
from src_0064 import task_func

def test_task_func():
    car_dict = {'Car1': 'Red', 'Car2': 'Blue', 'Car3': 'Red', 'Car4': 'Green', 'Car5': 'Blue'}
    df, ax = task_func(car_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (5, 2)
    assert list(df['Color']) == ['Red', 'Blue', 'Red', 'Green', 'Blue']
    assert list(df['Car']) == ['Car1', 'Car2', 'Car3', 'Car4', 'Car5']
    assert ax.get_xlabel() == 'Color'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Distribution of Vehicle Colors'