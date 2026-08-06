import matplotlib.pyplot as plt
import pandas as pd
from src_0064 import task_func


def test_task_func():
    car_dict = {"car1": "red", "car2": "blue", "car3": "green", "car4": "red", "car5": "blue"}
    df, ax = task_func(car_dict)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    assert df.columns.tolist() == ['Car', 'Color']
    assert df.shape == (5, 2)

    assert color_counts.keys().tolist() == ['red', 'blue', 'green']
    assert color_counts.values.tolist() == [2, 2, 1]

    assert ax.get_xlabel() == "Color"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Distribution of Vehicle Colors"