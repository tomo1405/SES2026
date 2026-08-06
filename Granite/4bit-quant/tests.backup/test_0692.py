import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
def task_func(df):
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df.values)
    df_std = pd.DataFrame(df_std, columns=df.columns)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(df_std)
    labels = kmeans.labels_
    return labels
import pytest
def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 9, 8, 7, 6]
    })
    
    # Call the function and store the result
    labels = task_func(df)
    
    # Assert that the result is a numpy array with the correct shape
    assert isinstance(labels, np.ndarray)
    assert labels.shape == (5,)
    
    # Assert that the labels are in the correct range
    assert labels.min() >= 0
    assert labels.max() < 3