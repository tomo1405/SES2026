import pytest
from src_0541 import task_func

def test_task_func():
    # Test case 1: Empty list
    list_of_menuitems = []
    title = "Menu Distribution"
    color = "blue"
    width = 1.0
    ax = task_func(list_of_menuitems, title, color, width)
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == title
    assert ax.get_xticklabels() == []
    assert ax.get_yticklabels() == []

    # Test case 2: Single list
    list_of_menuitems = [["Item 1", "Item 2", "Item 3"]]
    title = "Menu Distribution"
    color = "blue"
    width = 1.0
    ax = task_func(list_of_menuitems, title, color, width)
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == title
    assert ax.get_xticklabels() == ["Item 1", "Item 2", "Item 3"]
    assert ax.get_yticklabels() == [1, 1, 1]

    # Test case 3: Multiple lists
    list_of_menuitems = [["Item 1", "Item 2", "Item 3"], ["Item 4", "Item 5", "Item 6"]]
    title = "Menu Distribution"
    color = "blue"
    width = 1.0
    ax = task_func(list_of_menuitems, title, color, width)
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == title
    assert ax.get_xticklabels() == ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
    assert ax.get_yticklabels() == [2, 2, 2, 2, 2, 2]

    # Test case 4: Custom title
    list_of_menuitems = [["Item 1", "Item 2", "Item 3"], ["Item 4", "Item 5", "Item 6"]]
    title = "Custom Title"
    color = "blue"
    width = 1.0
    ax = task_func(list_of_menuitems, title, color, width)
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == title
    assert ax.get_xticklabels() == ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
    assert ax.get_yticklabels() == [2, 2, 2, 2, 2, 2]

    # Test case 5: Custom color
    list_of_menuitems = [["Item 1", "Item 2", "Item 3"], ["Item 4", "Item 5", "Item 6"]]
    title = "Menu Distribution"
    color = "red"
    width = 1.0
    ax = task_func(list_of_menuitems, title, color, width)
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == title
    assert ax.get_xticklabels() == ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
    assert ax.get_yticklabels() == [2, 2, 2, 2, 2, 2]

    # Test case 6: Custom width
    list_of_menuitems = [["Item 1", "Item 2", "Item 3"], ["Item 4", "Item 5", "Item 6"]]
    title = "Menu Distribution"
    color = "blue"
    width = 2.0
    ax = task_func(list_of_menuitems, title, color, width)
    assert ax.get_xlabel() == "Menu Items"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == title
    assert ax.get_xticklabels() == ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6"]
    assert ax.get_yticklabels() == [2, 2, 2, 2, 2, 2]