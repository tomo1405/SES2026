import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
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
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target

    # Mock the return value of sns.pairplot()
    pair_plot = sns.pairplot(iris_df, hue='species', vars=iris.feature_names)
    pair_plot.fig.suptitle('Iris Dataset Pair Plot', fontsize=16)  # Title for the figure

    # Call the task_func() and assert that the returned value is equal to the mocked value
    assert task_func() == pair_plot.fig