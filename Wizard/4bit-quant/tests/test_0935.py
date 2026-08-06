python
import hashlib
from collections import Counter
from src_0935 import task_func

def test_task_func():
    word = "hello"
    pairs = list(map(''.join, zip(word[:-1], word[1:])))
    pairs_count = dict(Counter(pairs))
    assert task_func(word) == hashlib.md5(str(pairs_count).encode()).hexdigest()