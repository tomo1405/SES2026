import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
import pytest

def task_func():
    plt.rc('font', family='Arial')  # Set the global font to Arial.
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target

    # Create a pair plot with the hue set to species.
    pair_plot = sns.pairplot(iris_df, hue='species', vars=iris.feature_names)
    pair_plot.fig.suptitle('Iris Dataset Pair Plot', fontsize=16)  # Title for the figure
    return pair_plot.fig

def test_task_func():
    # Mock the return value of load_iris()
    iris = load_iris()
    iris.data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    iris.feature_names = ['feature1', 'feature2', 'feature3']
    iris.target = [0, 1, 0]

    # Call the function and assert that the returned figure has the expected size
    fig = task_func()
    assert fig.get_size_inches() == (16, 12)

    # Call the function again and assert that the returned figure has the expected title
    fig = task_func()
    assert fig.axes[0, 0].get_title() == 'Iris Dataset Pair Plot'