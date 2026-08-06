python
import re
import string
from random import choice
import pytest

def task_func(n, pattern):
    while True:
        s = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, s):
            return s

def test_task_func():
    # Test case 1
    assert task_func(5, r'[a-zA-Z]{5}') == 'Qd23E'

    # Test case 2
    assert task_func(10, r'[a-zA-Z]{10}') == 'Qd23EghijKl'

    # Test case 3
    assert task_func(15, r'[a-zA-Z]{15}') == 'Qd23EghijKlMnop'

    # Test case 4
    assert task_func(20, r'[a-zA-Z]{20}') == 'Qd23EghijKlMnopQrst'

    # Test case 5
    assert task_func(25, r'[a-zA-Z]{25}') == 'Qd23EghijKlMnopQrstUvwx'

    # Test case 6
    assert task_func(30, r'[a-zA-Z]{30}') == 'Qd23EghijKlMnopQrstUvwxYz'