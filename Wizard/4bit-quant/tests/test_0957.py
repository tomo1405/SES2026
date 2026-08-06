python
import pytest
from src_0957 import task_func

def test_task_func():
    # Test case 1
    text = "Hello, World!"
    assert task_func(text) == "He_llo__Worl__"

    # Test case 2
    text = "Python is awesome!"
    assert task_func(text) == "Pyth_n_is_aw_some"

    # Test case 3
    text = "Testing 123"
    assert task_func(text) == "Tes_ting_123"

    # Test case 4
    text = "This is a test"
    assert task_func(text, seed=42) == "Th_s_s_t_t_n_g_123"

    # Test case 5
    text = "This is a test"
    assert task_func(text, seed=123) == "Th_s_s_t_t_n_g_123"

    # Test case 6
    text = "This is a test"
    assert task_func(text, seed=None) != "Th_s_s_t_t_n_g_123"