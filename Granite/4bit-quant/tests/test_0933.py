import pytest
from collections import Counter
import re

def task_func(word: str) -> list:
    clean_word = re.sub('[^a-z]', '', word.lower())
    
    if len(clean_word) < 2:
        return []
    
    pairs = [clean_word[i:i+2] for i in range(len(clean_word) - 1)]
    pair_counter = Counter(pairs)
    most_common = pair_counter.most_common(1)
    
    return most_common

def test_task_func():
    assert task_func("Hello") == [("ll", 2)]
    assert task_func("World") == [("or", 2)]
    assert task_func("Python") == [("th", 2)]
    assert task_func("Data Science") == [("at", 2)]
    assert task_func("AI") == []

if __name__ == "__main__":
    pytest.main()