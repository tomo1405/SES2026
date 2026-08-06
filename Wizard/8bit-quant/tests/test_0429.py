python
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df1, df2):
    merged_df = pd.merge(df1, df2, on="id", how="outer")

    # Select only numeric columns from df1 (excluding 'id')
    numeric_features_df1 = df1.select_dtypes(
        include=["float64", "int64"]
    ).columns.tolist()
    if "id" in numeric_features_df1:
        numeric_features_df1.remove("id")

    # Scale only the numeric features of df1
    if not merged_df.empty and numeric_features_df1:
        scaler = StandardScaler()
        merged_df[numeric_features_df1] = scaler.fit_transform(
            merged_df[numeric_features_df1]
        )

    # Pair plot only for the numeric features of df1
    pair_plot = None
    if numeric_features_df1:
        pair_plot = sns.pairplot(merged_df[numeric_features_df1])

    return merged_df, pair_plot

def test_task_func():
    # Test case 1: Both dataframes have numeric columns
    df1 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    df2 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_merged_df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_pair_plot = None
    actual_merged_df, actual_pair_plot = task_func(df1, df2)
    assert expected_merged_df.equals(actual_merged_df)
    assert expected_pair_plot == actual_pair_plot

    # Test case 2: df1 has numeric columns, df2 has non-numeric columns
    df1 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    df2 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": ["a", "b", "c", "d", "e"],
        "col2": [True, False, True, False, True],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_merged_df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_pair_plot = None
    actual_merged_df, actual_pair_plot = task_func(df1, df2)
    assert expected_merged_df.equals(actual_merged_df)
    assert expected_pair_plot == actual_pair_plot

    # Test case 3: df1 has non-numeric columns, df2 has numeric columns
    df1 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": ["a", "b", "c", "d", "e"],
        "col2": [True, False, True, False, True],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    df2 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_merged_df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "col2": [5.0, 4.0, 3.0, 2.0, 1.0],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_pair_plot = None
    actual_merged_df, actual_pair_plot = task_func(df1, df2)
    assert expected_merged_df.equals(actual_merged_df)
    assert expected_pair_plot == actual_pair_plot

    # Test case 4: Both dataframes have non-numeric columns
    df1 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": ["a", "b", "c", "d", "e"],
        "col2": [True, False, True, False, True],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    df2 = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1": ["a", "b", "c", "d", "e"],
        "col2": [True, False, True, False, True],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_merged_df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "col1_x": ["a", "b", "c", "d", "e"],
        "col1_y": ["a", "b", "c", "d", "e"],
        "col2_x": [True, False, True, False, True],
        "col2_y": [True, False, True, False, True],
        "col3": [10.0, 20.0, 30.0, 40.0, 50.0]
    })
    expected_pair_plot = None
    actual_merged_df, actual_pair_plot = task_func(df1, df2)
    assert expected_merged_df.equals(actual_merged_df)
    assert expected_pair_plot == actual_pair_plot