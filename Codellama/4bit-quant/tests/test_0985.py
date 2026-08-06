import pandas as pd
from src_0985 import task_func


def test_task_func():
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]})
    x_column = "x"
    y_column = "y"

    ax = task_func(df, x_column, y_column)

    assert ax.get_xlabel() == x_column
    assert ax.get_ylabel() == y_column
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_color() == "red"