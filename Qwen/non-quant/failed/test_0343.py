import pytest
from src_0343 import task_func

def test_task_func_no_match():
    elements = ['test', 'example']
    pattern = r'\d+'
    expected_replaced_elements = ['%WJ%', '%QZ%']
    expected_match = False
    
    replaced_elements, match = task_func(elements, pattern)
    
    assert replaced_elements == expected_replaced_elements
    assert match == expected_match

def test_task_func_match():
    elements = ['test', 'example']
    pattern = r'[a-zA-Z]+'
    expected_replaced_elements = ['%WJ%', '%QZ%']
    expected_match = True
    
    replaced_elements, match = task_func(elements, pattern)
    
    assert replaced_elements == expected_replaced_elements
    assert match == expected_match

def test_task_func_empty_elements():
    elements = []
    pattern = r'[a-zA-Z]+'
    expected_replaced_elements = []
    expected_match = False
    
    replaced_elements, match = task_func(elements, pattern)
    
    assert replaced_elements == expected_replaced_elements
    assert match == expected_match

def test_task_func_empty_pattern():
    elements = ['test', 'example']
    pattern = ''
    expected_replaced_elements = ['%WJ%', '%QZ%']
    expected_match = True  # An empty pattern will always match
    
    replaced_elements, match = task_func(elements, pattern)
    
    assert replaced_elements == expected_replaced_elements
    assert match == expected_match

def test_task_func_different_seed():
    elements = ['test', 'example']
    pattern = r'[a-zA-Z]+'
    seed = 200
    expected_replaced_elements = ['%XK%', '%LH%']
    expected_match = True
    
    replaced_elements, match = task_func(elements, pattern, seed)
    
    assert replaced_elements == expected_replaced_elements
    assert match == expected_match