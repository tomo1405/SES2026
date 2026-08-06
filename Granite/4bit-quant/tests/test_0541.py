import pytest
from src_0541 import task_func

def test_task_func():
    list_of_menuitems = [['burger', 'fries', 'salad'], ['soda', 'water', 'milk']]
    ax = task_func(list_of_menuitems)
    assert ax is not None
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Menu Distribution"

def test_task_func_with_title():
    list_of_menuitems = [['burger', 'fries', 'salad'], ['soda', 'water', 'milk']]
    ax = task_func(list_of_menuitems, title="My Menu Distribution")
    assert ax is not None
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "My Menu Distribution"

def test_task_func_with_color():
    list_of_menuitems = [['burger', 'fries', 'salad'], ['soda', 'water', 'milk']]
    ax = task_func(list_of_menuitems, color="red")
    assert ax is not None
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Menu Distribution"

def test_task_func_with_width():
    list_of_menuitems = [['burger', 'fries', 'salad'], ['soda', 'water', 'milk']]
    ax = task_func(list_of_menuitems, width=0.5)
    assert ax is not None
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Menu Distribution"