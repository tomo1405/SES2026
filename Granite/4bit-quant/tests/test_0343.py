import string
import random
import re
from src_0343 import task_func

def test_task_func():
    elements = ['abc', 'def', 'ghi']
    pattern = r'[a-z]{3}'
    seed = 100
    replaced_elements, search_result = task_func(elements, pattern, seed)
    assert isinstance(replaced_elements, list)
    assert all(isinstance(element, str) for element in replaced_elements)
    assert isinstance(search_result, bool)
    assert len(replaced_elements) == len(elements)
    for element in replaced_elements:
        assert all(c in string.ascii_letters for c in element)
    concatenated_elements = ''.join(replaced_elements)
    assert re.search(pattern, concatenated_elements) is not None