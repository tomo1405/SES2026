import pandas as pd
import seaborn as sns
import pytest

def task_func(data):
    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    ax.set_title('Correlation Matrix')
    return ax

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ax = task_func(data)
    assert ax.get_title() == 'Correlation Matrix'
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_zlabel() == 'value'