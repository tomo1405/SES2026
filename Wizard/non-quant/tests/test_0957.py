python
import pytest
from src_0957 import task_func

def test_task_func():
    # Test case 1
    text = "Hello, World!"
    expected_output = "He_ll__Worl___"
    assert task_func(text) == expected_output

    # Test case 2
    text = "Python is awesome!"
    expected_output = "Pyth_n_is_awe_some"
    assert task_func(text) == expected_output

    # Test case 3
    text = "Testing 123"
    expected_output = "Tes_t_n_g___"
    assert task_func(text) == expected_output

    # Test case 4
    text = "Random text with punctuation!"
    expected_output = "Ran_dom_t_x_t_w_th_p_u_n_c_t_i_o_n"
    assert task_func(text) == expected_output

    # Test case 5
    text = "Random text with punctuation!", 123
    expected_output = "Ran_dom_t_x_t_w_th_p_u_n_c_t_i_o_n"
    assert task_func(text, seed=123) == expected_output