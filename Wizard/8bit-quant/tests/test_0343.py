python
import string
import random
import re
import pytest

def task_func(elements, pattern, seed=100):
    # Set the seed for reproducibility
    random.seed(seed)
    replaced_elements = []
    
    for element in elements:
        replaced = ''.join([random.choice(string.ascii_letters) for _ in element])
        formatted = '%{}%'.format(replaced)
        replaced_elements.append(formatted)
        
    # Concatenate all the formatted elements into a single string
    concatenated_elements = ''.join(replaced_elements)
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_elements)
    # Return the search result
    return replaced_elements, bool(search_result)

def test_task_func():
    # Test case 1: Valid input
    elements = ['hello', 'world']
    pattern = r'\w+'
    replaced_elements, search_result = task_func(elements, pattern)
    assert replaced_elements == ['%h%l%l%o%', '%w%o%r%l%d%']
    assert search_result == True
    
    # Test case 2: Invalid input
    elements = ['hello', 'world']
    pattern = r'\d+'
    replaced_elements, search_result = task_func(elements, pattern)
    assert replaced_elements == ['%h%l%l%o%', '%w%o%r%l%d%']
    assert search_result == False
    
    # Test case 3: Empty input
    elements = []
    pattern = r'\w+'
    replaced_elements, search_result = task_func(elements, pattern)
    assert replaced_elements == []
    assert search_result == False
    
    # Test case 4: Single element input
    elements = ['hello']
    pattern = r'\w+'
    replaced_elements, search_result = task_func(elements, pattern)
    assert replaced_elements == ['%h%l%l%o%']
    assert search_result == True
    
    # Test case 5: Multiple occurrences of pattern
    elements = ['hello', 'world', 'hello', 'world']
    pattern = r'\w+'
    replaced_elements, search_result = task_func(elements, pattern)
    assert replaced_elements == ['%h%l%l%o%', '%w%o%r%l%d%', '%h%l%l%o%', '%w%o%r%l%d%']
    assert search_result == True
    
    # Test case 6: Reproducibility
    elements = ['hello', 'world']
    pattern = r'\w+'
    replaced_elements_1, search_result_1 = task_func(elements, pattern, seed=100)
    replaced_elements_2, search_result_2 = task_func(elements, pattern, seed=100)
    assert replaced_elements_1 == replaced_elements_2
    assert search_result_1 == search_result_2
    
    # Test case 7: Different seed
    elements = ['hello', 'world']
    pattern = r'\w+'
    replaced_elements_1, search_result_1 = task_func(elements, pattern, seed=100)
    replaced_elements_2, search_result_2 = task_func(elements, pattern, seed=200)
    assert replaced_elements_1 != replaced_elements_2
    assert search_result_1 != search_result_2