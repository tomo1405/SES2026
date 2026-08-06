import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pytest

def task_func(df):
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df.values)
    df_std = pd.DataFrame(df_std, columns=df.columns)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df_std)
    labels = kmeans.labels_
    return labels

def test_task_func():
    # Test with a sample DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })
    expected_labels = [0, 0, 0]  # Expected labels for the sample DataFrame
    actual_labels = task_func(df)
    assert actual_labels.tolist() == expected_labels

    # Test with another sample DataFrame
    df = pd.DataFrame({
        'X': [10, 11, 12],
        'Y': [13, 14, 15],
        'Z': [16, 17, 18]
    })
    expected_labels = [1, 1, 1]  # Expected labels for the second sample DataFrame
    actual_labels = task_func(df)
    assert actual_labels.tolist() == expected_labels

if __name__ == "__main__":
    pytest.main()