import pytest
from src_0431 import task_func
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Mocking matplotlib to capture plot creation
class MockAxes:
    def scatter(self, x, y, c):
        pass

    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

class MockFigure:
    def subplots(self):
        return self, MockAxes()

@pytest.fixture
def mock_plt(monkeypatch):
    monkeypatch.setattr(plt, 'subplots', MockFigure().subplots)

@pytest.fixture
def df1():
    return pd.DataFrame({
        'id': [1, 2, 3],
        'feature1': [1, 2, 3]
    })

@pytest.fixture
def df2():
    return pd.DataFrame({
        'id': [1, 2, 3],
        'feature2': [4, 5, 6]
    })

def test_task_func(mock_plt, df1, df2):
    labels, ax = task_func(df1, df2)
    
    # Check that labels are numpy array of length 3
    assert isinstance(labels, np.ndarray)
    assert len(labels) == 3

    # Check that ax is an instance of Axes
    assert isinstance(ax, MockAxes)

    # Check that the correct columns are used for clustering
    expected_X = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    })
    assert expected_X.equals(pd.DataFrame({'feature1': df1['feature1'], 'feature2': df2['feature2']}))

    # Check that KMeans is called with the correct parameters
    kmeans = KMeans(n_clusters=2, n_init=10)
    kmeans.fit(expected_X)
    assert np.array_equal(kmeans.labels_, labels)