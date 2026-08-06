python
import pytest
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from src_0292 import task_func

def test_task_func():
    # Test case 1: Test with default seed
    mappable = task_func(0, 1)
    assert isinstance(mappable, plt.cm.ScalarMappable)
    assert mappable.get_cmap().name == 'rocket_r'
    plt.close()

    # Test case 2: Test with custom seed
    mappable = task_func(0, 1, seed=42)
    assert isinstance(mappable, plt.cm.ScalarMappable)
    assert mappable.get_cmap().name == 'rocket_r'
    plt.close()

    # Test case 3: Test with mu=1, sigma=2
    mappable = task_func(1, 2)
    assert isinstance(mappable, plt.cm.ScalarMappable)
    assert mappable.get_cmap().name == 'rocket_r'
    plt.close()

    # Test case 4: Test with mu=-1, sigma=0.5
    mappable = task_func(-1, 0.5)
    assert isinstance(mappable, plt.cm.ScalarMappable)
    assert mappable.get_cmap().name == 'rocket_r'
    plt.close()