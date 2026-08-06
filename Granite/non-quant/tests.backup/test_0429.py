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
        'feature3': [13.4, 14.6, 15.8],
        'feature4': [16, 17, 18]
    })
    expected_merged_df = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [4.5, 6.7, 8.9],
        'feature2': [10, 11, 12],
        'feature3': [13.4, 14.6, 15.8],
        'feature4': [16, 17, 18]
    })
    expected_numeric_features_df1 = ['feature1', 'feature2']
    expected_pair_plot = sns.pairplot(expected_merged_df[expected_numeric_features_df1])

    merged_df, pair_plot = task_func(df1, df2)

    assert merged_df.equals(expected_merged_df)
    assert pair_plot.equals(expected_pair_plot)

if __name__ == "__main__":
    pytest.main()