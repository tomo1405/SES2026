import pytest
from src_0394 import task_func

def test_task_func():
    fig = task_func(mu=0, sigma=1)
    assert fig is not None
    assert fig.get_size_inches() == (12, 6)

def test_task_func_with_seed():
    fig1 = task_func(mu=0, sigma=1, seed=77)
    fig2 = task_func(mu=0, sigma=1, seed=77)
    assert fig1.get_size_inches() == fig2.get_size_inches()

def test_task_func_with_num_samples():
    fig1 = task_func(mu=0, sigma=1, num_samples=1000)
    fig2 = task_func(mu=0, sigma=1, num_samples=2000)
    assert fig1.get_size_inches() != fig2.get_size_inches()