import pytest
from src_0921 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    ax.set_title('Correlation Matrix')
    expected_output = ax
    actual_output = task_func(data)
    assert actual_output == expected_output