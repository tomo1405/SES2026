python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def task_func(data, n_components=2):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("data should be a DataFrame.")

    if not data.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all():
        raise ValueError("DataFrame should only contain numeric values.")
    
    if n_components > len(data.columns):
        raise ValueError("n_components should not be greater than the number of columns in data.")
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    pca = PCA(n_components=n_components)
    data_reduced = pca.fit_transform(data_scaled)
    return pd.DataFrame(data_reduced)

def test_task_func():
    # Test case 1: Valid input
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 2
    expected_result = pd.DataFrame({'PC1': [-0.70710678, -0.70710678], 'PC2': [-0.70710678, 0.70710678]})
    result = task_func(data, n_components)
    assert result.equals(expected_result)

    # Test case 2: Invalid input: data should be a DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    n_components = 2
    with pytest.raises(ValueError, match="data should be a DataFrame."):
        task_func(data, n_components)

    # Test case 3: Invalid input: DataFrame should only contain numeric values
    data = pd.DataFrame({'A': [1, 2, '3'], 'B': [4, 5, 6]})
    n_components = 2
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data, n_components)

    # Test case 4: Invalid input: n_components should not be greater than the number of columns in data
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 3
    with pytest.raises(ValueError, match="n_components should not be greater than the number of columns in data."):
        task_func(data, n_components)