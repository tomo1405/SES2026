import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pytest

from src_0292 import task_func

def test_task_func_seed():
    mu = 0
    sigma = 1
    seed = 0
    mappable = task_func(mu, sigma, seed)
    assert isinstance(mappable, sns.axisgrid.Grid)
    assert len(plt.gcf().axes) == 2

def test_task_func_default_seed():
    mu = 0
    sigma = 1
    mappable = task_func(mu, sigma)
    assert isinstance(mappable, sns.axisgrid.Grid)
    assert len(plt.gcf().axes) == 2

def test_task_func_seed_type():
    mu = 0
    sigma = 1
    seed = "not_an_integer"
    with pytest.raises(TypeError):
        task_func(mu, sigma, seed)

def test_task_func_seed_value():
    mu = 0
    sigma = 1
    seed = -1
    with pytest.raises(ValueError):
        task_func(mu, sigma, seed)