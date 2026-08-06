import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pytest

def task_func(df):

    # Data preparation

    if df.empty:
        return 0,0

    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    
    # Performing PCA
    pca = PCA()
    pca.fit(df.iloc[:,1:])
    
    # Extracting explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Creating bar chart
    fig, ax = plt.subplots()
    ax.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
    ax.set_title('Explained Variance Ratio of Principal Components')
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    
    return explained_variance_ratio, ax

# Example test cases
def test_task_func():
    # Test case 1: df is not empty
    df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
                       'Value': [10, 20, 30]})
    expected_output = ([0.5, 0.25, 0.125], <matplotlib.axes._subplots.AxesSubplot object at 0x7f8d5d28c1d0>)
    actual_output = task_func(df)
    assert actual_output == expected_output

    # Test case 2: df is empty
    df = pd.DataFrame()
    expected_output = (0,0)
    actual_output = task_func(df)
    assert actual_output == expected_output