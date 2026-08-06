python
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency
import pytest

def task_func(df1, df2, column1="feature1", column2="feature2"):
    df = pd.merge(df1, df2, on="id")
    contingency_table = pd.crosstab(df[column1], df[column2])
    heatmap = sns.heatmap(contingency_table)
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p, heatmap

def test_task_func():
    df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': ['A', 'B', 'C'], 'feature2': [1, 2, 3]})
    df2 = pd.DataFrame({'id': [1, 2, 3], 'feature1': ['A', 'B', 'C'], 'feature2': [1, 2, 3]})
    p, heatmap = task_func(df1, df2)
    assert p == 1.0
    assert isinstance(heatmap, sns.matrix.ClusterGrid)