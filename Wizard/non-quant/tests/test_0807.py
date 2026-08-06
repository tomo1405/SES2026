python
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def test_task_func():
    # Test case 1
    text = "This is a test sentence."
    n = 2
    expected_result = Counter([('is', 'a'), ('a', 'test'), ('test', 'sentence'), ('sentence', '.')])
    assert task_func(text, n) == expected_result

    # Test case 2
    text = "The quick brown fox jumps over the lazy dog."
    n = 3
    expected_result = Counter([('the', 'quick', 'brown'), ('quick', 'brown', 'fox'), ('brown', 'fox', 'jumps'), ('fox', 'jumps', 'over'), ('jumps', 'over', 'the'), ('over', 'the', 'lazy'), ('the', 'lazy', 'dog'), ('lazy', 'dog', '.'), ('.', '.', '.')])
    assert task_func(text, n) == expected_result

    # Test case 3
    text = "Python is a high-level programming language."
    n = 4
    expected_result = Counter([('python', 'is', 'a', 'high'), ('is', 'a', 'high', 'level'), ('a', 'high', 'level', 'programming'), ('high', 'level', 'programming', 'language'), ('level', 'programming', 'language', '.'), ('programming', 'language', '.', '.', '.'), ('language', '.', '.', '.', '.')])
    assert task_func(text, n) == expected_result