import pytest
from src_0530 import task_func
from collections import Counter

def test_task_func_with_default_parameters():
    num_rolls = 100
    num_dice = 2
    sums_counter, ax = task_func(num_rolls, num_dice)
    assert isinstance(sums_counter, Counter)
    assert len(sums_counter) >= 2 and len(sums_counter) <= 12

def test_task_func_with_custom_random_seed():
    num_rolls = 100
    num_dice = 2
    random_seed = 42
    sums_counter_1, _ = task_func(num_rolls, num_dice, random_seed=random_seed)
    sums_counter_2, _ = task_func(num_rolls, num_dice, random_seed=random_seed)
    assert sums_counter_1 == sums_counter_2

def test_task_func_with_plot_path():
    num_rolls = 100
    num_dice = 2
    plot_path = "test_plot.png"
    _, ax = task_func(num_rolls, num_dice, plot_path=plot_path)
    assert ax is not None
    # Additional check to ensure file exists can be added here if needed

def test_task_func_with_single_die():
    num_rolls = 100
    num_dice = 1
    sums_counter, ax = task_func(num_rolls, num_dice)
    assert isinstance(sums_counter, Counter)
    assert set(sums_counter.keys()) == set(range(1, 7))

def test_task_func_with_multiple_dice():
    num_rolls = 100
    num_dice = 3
    sums_counter, ax = task_func(num_rolls, num_dice)
    assert isinstance(sums_counter, Counter)
    assert set(sums_counter.keys()) == set(range(3, 19))