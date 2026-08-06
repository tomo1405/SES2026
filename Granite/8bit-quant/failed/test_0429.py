import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df1, df2):
    merged_df = pd.merge(df1, df2, on="id", how="outer")

    numeric_features_df1 = df1.select_dtypes(
        include=["float64", "int64"]
    ).columns.tolist()
    if "id" in numeric_features_df1:
        numeric_features_df1.remove("id")

    if not merged_df.empty and numeric_features_df1:
        scaler = StandardScaler()
        merged_df[numeric_features_df1] = scaler.fit_transform(
            merged_df[numeric_features_df1]
        )

    pair_plot = None
    if numeric_features_df1:
        pair_plot = sns.pairplot(merged_df[numeric_features_df1])

    return merged_df, pair_plot

def test_task_func():
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [4.5, 6.7, 8.9],
        'feature2': [10, 11, 12]
    })
    df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature3': [13, 14, 15],
        'feature4': [16.7, 18.9, 20.1]
    })
    merged_df, pair_plot = task_func(df1, df2)
    assert isinstance(merged_df, pd.DataFrame)
    assert isinstance(pair_plot, sns.axisgrid.PairGrid)

def test_task_func_empty_df():
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [4.5, 6.7, 8.9],
        'feature2': [10, 11, 12]
    })
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert isinstance(merged_df, pd.DataFrame)
    assert pair_plot is None

def test_task_func_no_numeric_features():
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': ['a', 'b', 'c'],
        'feature2': ['d', 'e', 'f']
    })
    df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature3': [13, 14, 15],
        'feature4': [16.7, 18.9, 20.1]
    })
    merged_df, pair_plot = task_func(df1, df2)
    assert isinstance(merged_df, pd.DataFrame)
    assert pair_plot is None