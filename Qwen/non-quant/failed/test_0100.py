import pytest
from src_0100 import task_func
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def test_task_func():
    fig = task_func()
    
    # Check if the returned object is a matplotlib Figure
    assert isinstance(fig, plt.Figure), "The function should return a matplotlib Figure object."
    
    # Check if the figure has the correct title
    assert fig._suptitle.get_text() == 'Iris Dataset Pair Plot', "The figure title is incorrect."
    
    # Check if the figure has the correct number of subplots
    axes = fig.axes
    assert len(axes) == 12, "The figure should have 12 subplots (4x3 grid)."
    
    # Check if the subplots have the correct data
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target
    
    for i, ax in enumerate(axes):
        x_var = iris.feature_names[i // 4]
        y_var = iris.feature_names[i % 4]
        data = iris_df[[x_var, y_var, 'species']]
        
        # Check if the scatter plots are correctly created
        for species in range(3):
            subset = data[data['species'] == species]
            sns.scatterplot(ax=ax, x=x_var, y=y_var, data=subset, hue='species')
    
    # Check if the plot is displayed correctly
    plt.show()