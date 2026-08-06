import pytest
from src_0547 import task_func
from collections import OrderedDict
from prettytable import PrettyTable

def test_task_func():
    # Test case 1
    my_dict = {'b': 2, 'a': 1, 'c': 3}
    result = task_func(my_dict=my_dict)
    assert result.get_string() == '+-----+-----+\n| Key | Value |\n+-----+-----+\n| a   | 1     |\n| b   | 2     |\n| c   | 3     |\n+-----+-----+\n'

    # Add more test cases as needed

# Add more test cases as needed