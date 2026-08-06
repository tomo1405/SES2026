from collections import Counter
import hashlib
def task_func(word: str) -> dict:
    pairs = list(map(''.join, zip(word[:-1], word[1:])))
    pairs_count = dict(Counter(pairs))
    # encode the dictionary as a string and return its hash
    return hashlib.md5(str(pairs_count).encode()).hexdigest()