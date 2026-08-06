from unittest.mock import patch

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA


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

def test_task_func():
    # Mocking the input dataframe
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Value': [10, 20, 30]})

    # Mocking the expected output
    expected_output = (pca.explained_variance_ratio_, ax)

    # Mocking the PCA and matplotlib.pyplot modules
    with patch('src_0305.PCA') as mock_PCA, patch('src_0305.plt.bar') as mock_bar:
        mock_PCA.return_value.explained_variance_ratio_ = [0.5, 0.3, 0.2]
        mock_bar.return_value = None

        # Calling the function under test
        output = task_func(df)

        # Asserting that the output matches the expected output
        assert output == expected_output