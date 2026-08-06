import pytest
from src_0957 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    assert task_func("Hello, World!", seed=42) == "H_e_l_l_o__W_o_r_l_d_!"

    # Add more test cases as needed