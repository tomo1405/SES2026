import pytest
from src_0929 import task_func

def test_task_func():
    assert task_func("abc") == {'aa': 0, 'ab': 1, 'ac': 0, 'ba': 1, 'bb': 0, 'bc': 0, 'ca': 0, 'cb': 0, 'cc': 0}
    assert task_func("aabbcc") == {'aa': 1, 'ab': 2, 'ac': 0, 'ba': 1, 'bb': 2, 'bc': 0, 'ca': 0, 'cb': 0, 'cc': 0}
    assert task_func("abcabc") == {'aa': 0, 'ab': 2, 'ac': 0, 'ba': 2, 'bb': 0, 'bc': 2, 'ca': 0, 'cb': 0, 'cc': 0}