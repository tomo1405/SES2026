import pytest
from src_0703 import task_func
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'feature1': [1, 2, 3, 4],
        'feature2': [5, 6, 7, 8]
    }
    df = pd.DataFrame(data)

    # Call the function
    result = task_func(df=df)

    # Check the output
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (4, 2), "The result should have 2 columns"
    assert list(result.columns) == ['PC1', 'PC2'], "The columns should be named 'PC1' and 'PC2'"