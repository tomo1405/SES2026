import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from unittest.mock import patch

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
    with patch('matplotlib.pyplot.rc') as mock_rc:
        with patch('seaborn.pairplot') as mock_pairplot:
            fig = task_func()
            mock_rc.assert_called_once_with('font', family='Arial')
            mock_pairplot.assert_called_once()
            assert fig == mock_pairplot.return_value.fig