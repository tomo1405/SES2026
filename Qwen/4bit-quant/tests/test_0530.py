from io import BytesIO
from typing import Counter

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0530 import task_func


@pytest.fixture
def setup_plot():
    plt.switch_backend('Agg')  # Use non-interactive backend for testing

@pytest.mark.usefixtures("setup_plot")
def test_task_func_no_plot():
    num_rolls = 1000
    num_dice = 2
    random_seed = 42
    result, ax = task_func(num_rolls, num_dice, random_seed=random_seed)
    
    assert isinstance(result, Counter)
    assert len(result) >= 2 and len(result) <= 12  # Possible sums range from 2 to 12
    assert sum(result.values()) == num_rolls

@pytest.mark.usefixtures("setup_plot")
def test_task_func_with_plot():
    num_rolls = 1000
    num_dice = 2
    random_seed = 42
    plot_path = BytesIO()
    result, ax = task_func(num_rolls, num_dice, plot_path=plot_path, random_seed=random_seed)
    
    assert isinstance(result, Counter)
    assert len(result) >= 2 and len(result) <= 12  # Possible sums range from 2 to 12
    assert sum(result.values()) == num_rolls
    
    # Check if the plot was saved correctly
    plot_path.seek(0)
    img = plt.imread(plot_path)
    assert isinstance(img, np.ndarray)

@pytest.mark.usefixtures("setup_plot")
def test_task_func_invalid_random_seed():
    with pytest.raises(ValueError):
        task_func(1000, 2, random_seed=-1)

@pytest.mark.usefixtures("setup_plot")
def test_task_func_zero_rolls():
    with pytest.raises(ValueError):
        task_func(0, 2)

@pytest.mark.usefixtures("setup_plot")
def test_task_func_zero_dice():
    with pytest.raises(ValueError):
        task_func(1000, 0)