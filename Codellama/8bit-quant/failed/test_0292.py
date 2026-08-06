import pytest
from src_0292 import task_func
import numpy as np
import seaborn as sns

def test_task_func():
    # Test with valid inputs
    mu = 0
    sigma = 1
    seed = 0
    mappable = task_func(mu, sigma, seed)
    assert isinstance(mappable, sns.kdeplot)
    assert mappable.collections[0].get_label() == 'Density'

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func(mu, sigma, seed, fill=False)

    with pytest.raises(ValueError):
        task_func(mu, sigma, seed, color='red')

    with pytest.raises(ValueError):
        task_func(mu, sigma, seed, alpha=0.5)