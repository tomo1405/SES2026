import pytest
from src_0703 import task_func
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1.0, 2.0, 3.0],
        'feature2': [4.0, 5.0, 6.0],
        'feature3': [7.0, 8.0, 9.0]
    }
    df = pd.DataFrame(data)
    
    # Expected result after PCA transformation
    expected_columns = ['PC1', 'PC2']
    
    # Call the function
    result_df = task_func(df)
    
    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame), "The result should be a pandas DataFrame."
    
    # Check if the DataFrame has the correct columns
    assert list(result_df.columns) == expected_columns, "The DataFrame should have columns 'PC1' and 'PC2'."
    
    # Check if the DataFrame has the correct shape
    assert result_df.shape == (3, 2), "The DataFrame should have 3 rows and 2 columns."
    
    # Check if the PCA transformation was applied correctly
    pca = PCA(n_components=2)
    expected_result = pca.fit_transform(df)
    assert all(result_df.iloc[:, 0] == expected_result[:, 0]), "The first principal component does not match."
    assert all(result_df.iloc[:, 1] == expected_result[:, 1]), "The second principal component does not match."

# Run the tests
if __name__ == "__main__":
    pytest.main()