python
import hashlib
from collections import Counter
from src_0935 import task_func

def test_task_func():
    word = "hello"
    pairs = list(map(''.join, zip(word[:-1], word[1:])))
    pairs_count = dict(Counter(pairs))
    expected_hash = hashlib.md5(str(pairs_count).encode()).hexdigest()
    assert task_func(word) == expected_hash