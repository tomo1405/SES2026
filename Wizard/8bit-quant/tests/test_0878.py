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
    # Test case 1: valid input
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = task_func(data, n_components=2)
    assert result.shape == (3, 2)
    assert result.iloc[0, 0] == pytest.approx(-0.936, 0.01)
    assert result.iloc[0, 1] == pytest.approx(-0.342, 0.01)

    # Test case 2: invalid input (not a DataFrame)
    with pytest.raises(ValueError):
        task_func([1, 2, 3], n_components=2)

    # Test case 3: invalid input (not numeric)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']}), n_components=2)

    # Test case 4: invalid input (n_components > number of columns)
    with pytest.raises(ValueError):
        task_func(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}), n_components=3)