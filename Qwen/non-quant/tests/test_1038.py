import pytest
from src_1038 import task_func
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_input_types():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    with pytest.raises(ValueError):
        task_func(1, s2)
    with pytest.raises(ValueError):
        task_func(s1, "string")

def test_task_func_input_lengths():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5])
    with pytest.raises(ValueError):
        task_func(s1, s2)

def test_task_func_output():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    labels, ax = task_func(s1, s2, n_clusters=2)
    assert isinstance(labels, list)
    assert len(labels) == len(s1)
    assert all(isinstance(label, int) for label in labels)
    assert isinstance(ax, plt.Axes)

def test_task_func_plot():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([4, 5, 6])
    _, ax = task_func(s1, s2, n_clusters=2)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert len(img_base64) > 0