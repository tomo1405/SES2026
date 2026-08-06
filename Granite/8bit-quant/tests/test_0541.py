import pytest
from src_0541 import task_func

def test_task_func():
    list_of_menuitems = [['Pizza', 'Pasta', 'Pizza', 'Pasta'], ['Burger', 'Salad', 'Burger', 'Salad', 'Burger']]
    ax = task_func(list_of_menuitems)
    assert ax is not None
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Menu Distribution"