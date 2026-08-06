import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

LETTERS = list(string.ascii_lowercase)

def task_func(rows=1000, string_length=3):
    data = ["".join(random.choices(LETTERS, k=string_length)) for _ in range(rows)]
    df = pd.DataFrame({"String": data})
    if df.empty:
        print("No data to generate heatmap.")
        return None
    df = pd.get_dummies(df["String"].apply(list).explode()).groupby(level=0).sum()
    corr = df.corr()
    ax = sns.heatmap(corr, annot=True, fmt=".2f")
    plt.close()
    return ax

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_params():
    ax = task_func(rows=500, string_length=5)
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_empty_data():
    ax = task_func(rows=0, string_length=3)
    assert ax is None