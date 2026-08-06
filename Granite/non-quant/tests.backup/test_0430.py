import pandas as pd
import pytest
from sklearn.feature_selection import SelectKBest, f_classif
import seaborn as sns

def task_func(df1, df2):
    # Merge dataframes based on 'id'
    df = pd.merge(df1, df2, on="id")

    # Separate features and target
    features = df1.columns.drop("id")
    X = df[features]
    y = df["target"]

    # Select top 2 features
    selector = SelectKBest(f_classif, k=2)
    X_new = selector.fit_transform(X, y)

    selected_features = [x for x, y in zip(features, selector.get_support()) if y]

    # Draw heatmap
    heatmap = sns.heatmap(
        pd.DataFrame(X_new, columns=selected_features).corr(), annot=True
    )

    return selected_features, heatmap

def test_task_func():
    # Create sample dataframes
    df1 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [4, 5, 6],
        'feature2': [7, 8, 9],
        'target': ['a', 'b', 'c']
    })
    df2 = pd.DataFrame({
        'id': [1, 2, 3],
        'feature3': [10, 11, 12],
        'feature4': [13, 14, 15],
        'target': ['d', 'e', 'f']
    })

    # Call the function
    selected_features, heatmap = task_func(df1, df2)

    # Check the output type
    assert isinstance(selected_features, list)
    assert isinstance(heatmap, sns.matrix.Heatmap)

    # Check the number of selected features
    assert len(selected_features) == 2

    # Check the correlation heatmap
    assert heatmap. annot == True