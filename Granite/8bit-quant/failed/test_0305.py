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

# Define a test DataFrame
test_df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Value': [10, 20, 30]
})

# Test the function with an empty DataFrame
empty_df_result = task_func(pd.DataFrame())
assert empty_df_result == (0, 0)

# Test the function with a non-empty DataFrame
non_empty_df_result = task_func(test_df)
assert len(non_empty_df_result[0]) == len(test_df.iloc[:,1:])
assert non_empty_df_result[1].get_title() == 'Explained Variance Ratio of Principal Components'
assert non_empty_df_result[1].get_xlabel() == 'Principal Component'
assert non_empty_df_result[1].get_ylabel() == 'Explained Variance Ratio'