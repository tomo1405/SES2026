import pytest
from src_0292 import task_func
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def test_task_func():
    # Test with default parameters
    mappable = task_func(0, 1)
    assert isinstance(mappable, sns.kdeplot.KDEPlot)
    assert len(mappable.collections) == 1
    assert isinstance(mappable.collections[0], plt.collections.PathCollection)

    # Test with custom parameters
    mappable = task_func(10, 2, seed=42)
    assert isinstance(mappable, sns.kdeplot.KDEPlot)
    assert len(mappable.collections) == 1
    assert isinstance(mappable.collections[0], plt.collections.PathCollection)

    # Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=0)
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=-1)
    with pytest.raises(ValueError):
        task_func(mu=0, sigma=100)