import pytest
import seaborn as sns
from scipy.stats import chi2_contingency
import pandas as pd

def task_func(df1, df2, column1="feature1", column2="feature2"):
    df = pd.merge(df1, df2, on="id")
    contingency_table = pd.crosstab(df[column1], df[column2])
    heatmap = sns.heatmap(contingency_table)
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p, heatmap

def test_task_func():
    # Test case 1: Test with valid input and expected output
    df1 = pd.DataFrame({"id": [1, 2, 3], "feature1": ["A", "B", "C"]})
    df2 = pd.DataFrame({"id": [1, 2, 3], "feature2": ["X", "Y", "Z"]})
    expected_p_value = 0.5
    expected_heatmap = "heatmap_object"
    actual_p_value, actual_heatmap = task_func(df1, df2)
    assert actual_p_value == expected_p_value
    assert actual_heatmap == expected_heatmap

    # Test case 2: Test with invalid input and expected exception
    with pytest.raises(ValueError):
        task_func(None, None)