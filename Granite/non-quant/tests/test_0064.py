import matplotlib.pyplot as plt
import pandas as pd
from src_0064 import task_func


def test_task_func():
    car_dict = {'Toyota': 'Red', 'Honda': 'Blue', 'Ford': 'Green'}
    df, ax = task_func(car_dict)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 2)
    assert df.columns.tolist() == ['Car', 'Color']
    assert df['Color'].value_counts().keys().tolist() == ['Red', 'Blue', 'Green']
    assert df['Color'].value_counts().values.tolist() == [1, 1, 1]
    assert ax.get_xlabel() == 'Color'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Distribution of Vehicle Colors'