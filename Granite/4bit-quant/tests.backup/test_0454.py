import re
import string
from random import choice
def task_func(n, pattern):
    while True:
        s = ''.join(choice(string.ascii_letters) for _ in range(n))
        if re.match(pattern, s):
            return s
import pytest

def test_task_func():
    n = 10
    pattern = r'[a-z]+'
    result = task_func(n, pattern)
    assert result is not None
    assert len(result) == n
    assert all(c in string.ascii_letters for c in result)
    assert re.match(pattern, result)

if __name__ == "__main__":
    pytest.main()