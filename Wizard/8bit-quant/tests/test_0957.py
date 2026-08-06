python
import pytest
from src_0957 import task_func

def test_task_func():
    # Test case 1
    text = "Hello, World!"
    expected_output = "He_ll__W_rld"
    assert task_func(text) == expected_output

    # Test case 2
    text = "Python is awesome!"
    expected_output = "Pyth_n_s_awe_om"
    assert task_func(text) == expected_output

    # Test case 3
    text = "Testing 123"
    expected_output = "T_stng_123"
    assert task_func(text) == expected_output

    # Test case 4
    text = "Random text with punctuation!"
    expected_output = "Rn_m_t_xt_w_p_nctn"
    assert task_func(text) == expected_output

    # Test case 5
    text = "Random text with punctuation!", 123
    expected_output = "Rn_m_t_xt_w_p_nctn"
    assert task_func(text, seed=123) == expected_output