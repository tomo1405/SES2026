import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_diabetes


def task_func():
    font = {'family': 'Arial'}
    plt.rc('font', **font)  # Set the global font to Arial.
    DIABETES = load_diabetes()
    diabetes_df = pd.DataFrame(data=DIABETES.data, columns=DIABETES.feature_names)
    pair_plot = sns.pairplot(diabetes_df)
    return pair_plot.fig, diabetes_df

def test_task_func():
    pair_plot_fig, diabetes_df = task_func()
    assert isinstance(pair_plot_fig, plt.Figure)
    assert isinstance(diabetes_df, pd.DataFrame)
    assert len(diabetes_df.columns) == 10
    assert list(diabetes_df.columns) == list(DIABETES.feature_names)