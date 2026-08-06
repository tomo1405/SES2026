import pytest
from src_0703 import task_func
import pandas as pd
from sklearn.decomposition import PCA

def test_task_func():
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    expected_df = pd.DataFrame({'PC1': [1, 2, 3], 'PC2': [4, 5, 6]})
    assert task_func(df).equals(expected_df)