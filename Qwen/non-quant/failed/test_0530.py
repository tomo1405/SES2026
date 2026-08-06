import pytest
from src_0530 import task_func
from collections import Counter
import matplotlib.pyplot as plt
import os

@pytest.fixture
def mock_random(monkeypatch):
    def mock_choice(seq):
        return 4  # Always return 4 for deterministic behavior
    monkeypatch.setattr(random, 'choice', mock_choice)

@pytest.fixture
def temp_plot_file(tmpdir):
    return str(tmpdir.join('test_plot.png'))

def test_task_func_output(mock_random):
    num_rolls = 10
    num_dice = 2
    sums_counter, ax = task_func(num_rolls, num_dice)
    expected_sums = [8] * num_rolls  # Since each die always rolls 4
    expected_counter = Counter(expected_sums)
    assert sums_counter == expected_counter

def test_task_func_plot(mock_random, temp_plot_file):
    num_rolls = 10
    num_dice = 2
    sums_counter, ax = task_func(num_rolls, num_dice, plot_path=temp_plot_file)
    assert os.path.exists(temp_plot_file), "Plot file was not created"
    plt.close(ax.figure)  # Close the plot to prevent memory leaks

def test_task_func_no_plot(mock_random):
    num_rolls = 10
    num_dice = 2
    sums_counter, ax = task_func(num_rolls, num_dice)
    assert ax is not None, "Axis object should be returned even if no plot path is provided"
    plt.close(ax.figure)  # Close the plot to prevent memory leaks

def test_task_func_with_seed():
    num_rolls = 10
    num_dice = 2
    random_seed = 42
    sums_counter_1, _ = task_func(num_rolls, num_dice, random_seed=random_seed)
    sums_counter_2, _ = task_func(num_rolls, num_dice, random_seed=random_seed)
    assert sums_counter_1 == sums_counter_2, "Function should produce the same results with the same seed"