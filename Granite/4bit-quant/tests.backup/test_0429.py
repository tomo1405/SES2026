import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
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
    # Test case 1: merged_df is empty and numeric_features_df1 is empty
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    merged_df, pair_plot = task_func(df1, df2)
    assert merged_df.empty
    assert pair_plot is None

    # Test case 2: merged_df is not empty and numeric_features_df1 is not empty
    df1 = pd.DataFrame({
        "id": [1, 2, 3],
        "feature1": [4.5, 6.7, 8.9],
        "feature2": [10, 11, 12]
    })
    df2 = pd.DataFrame({
        "id": [1, 2, 3],
        "feature3": [13, 14, 15]
    })
    merged_df, pair_plot = task_func(df1, df2)
    assert not merged_df.empty
    assert "feature1" in merged_df.columns
    assert "feature2" in merged_df.columns
    assert "feature3" in merged_df.columns
    assert pair_plot is not None

test_task_func()