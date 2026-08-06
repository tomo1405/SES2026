import pytest
from src_0554 import task_func

def test_task_func_empty_lists():
    a = []
    b = []
    fig, ax = task_func(a, b)
    assert fig is not None
    assert ax is not None
    plt.close(fig)

def test_task_func_non_empty_lists():
    a = [1, 2, 3]
    b = ['A', 'B', 'C']
    fig, ax = task_func(a, b)
    assert fig is not None
    assert ax is not None
    plt.close(fig)

def test_task_func_non_empty_lists_with_different_lengths():
    a = [1, 2, 3]
    b = ['A', 'B', 'C', 'D']
    fig, ax = task_func(a, b)
    assert fig is not None
    assert ax is not None
    plt.close(fig)

def test_task_func_non_empty_lists_with_duplicate_elements():
    a = [1, 2, 3]
    b = ['A', 'B', 'C', 'A']
    fig, ax = task_func(a, b)
    assert fig is not None
    assert ax is not None
    plt.close(fig)

def test_task_func_non_empty_lists_with_different_types():
    a = [1, 2, 3]
    b = ['A', 'B', 'C', 1]
    fig, ax = task_func(a, b)
    assert fig is not None
    assert ax is not None
    plt.close(fig)