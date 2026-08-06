import pytest
from src_0921 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    ax.set_title('Correlation Matrix')
    assert ax.get_title() == 'Correlation Matrix'
    assert ax.get_xlabel() == 'a'
    assert ax.get_ylabel() == 'b'
    assert ax.get_zlabel() == 'c'
    assert ax.get_zlim() == (0, 1)
    assert ax.get_cmap() == 'coolwarm'
    assert ax.get_annot() == True