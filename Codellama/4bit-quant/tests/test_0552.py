import pytest
from src_0552 import task_func

def test_task_func():
    # Test with an empty list
    assert task_func([]) is None

    # Test with a list of menu items
    menu_items = [['Pizza', 'Pasta', 'Sandwich'], ['Tacos', 'Salad', 'Soup']]
    ax = task_func(menu_items)
    assert ax is not None
    assert ax.get_xlabel() == 'Count'
    assert ax.get_ylabel() == 'Item'
    assert ax.get_title() == 'Menu Items'
    assert ax.get_legend() is None
    assert ax.get_xlim() == (0, 3)
    assert ax.get_ylim() == (0, 2)
    assert ax.get_xticks() == [1, 2, 3]
    assert ax.get_yticks() == ['Pizza', 'Pasta', 'Sandwich', 'Tacos', 'Salad', 'Soup']
    assert ax.get_xticklabels() == ['1', '2', '3']
    assert ax.get_yticklabels() == ['Pizza', 'Pasta', 'Sandwich', 'Tacos', 'Salad', 'Soup']

    # Test with a list of menu items with duplicates
    menu_items = [['Pizza', 'Pasta', 'Sandwich'], ['Tacos', 'Salad', 'Soup'], ['Pizza', 'Pasta', 'Sandwich']]
    ax = task_func(menu_items)
    assert ax is not None
    assert ax.get_xlabel() == 'Count'
    assert ax.get_ylabel() == 'Item'
    assert ax.get_title() == 'Menu Items'
    assert ax.get_legend() is None
    assert ax.get_xlim() == (0, 3)
    assert ax.get_ylim() == (0, 2)
    assert ax.get_xticks() == [1, 2, 3]
    assert ax.get_yticks() == ['Pizza', 'Pasta', 'Sandwich', 'Tacos', 'Salad', 'Soup']
    assert ax.get_xticklabels() == ['1', '2', '3']
    assert ax.get_yticklabels() == ['Pizza', 'Pasta', 'Sandwich', 'Tacos', 'Salad', 'Soup']