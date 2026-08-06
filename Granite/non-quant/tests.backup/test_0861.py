import re
import random
import string
import pytest
from src_0861 import task_func

@pytest.mark.parametrize("n, pattern, seed, expected_matches", [
    (10, r"\d", None, [str(random.randint(0, 9)) for _ in range(10)]),
    (20, r"[a-z]", None, [random.choice(string.ascii_lowercase) for _ in range(20)]),
    (30, r"[A-Z]", None, [random.choice(string.ascii_uppercase) for _ in range(30)]),
    (40, r"[0-9A-Za-z]", None, [random.choice(string.ascii_letters + string.digits) for _ in range(40)]),
    (50, r"[^0-9A-Za-z]", None, [random.choice(string.punctuation) for _ in range(50)]),
    (10, r"\d", 12345, [str(random.randint(0, 9)) for _ in range(10)]),
    (20, r"[a-z]", 12345, [random.choice(string.ascii_lowercase) for _ in range(20)]),
    (30, r"[A-Z]", 12345, [random.choice(string.ascii_uppercase) for _ in range(30)]),
    (40, r"[0-9A-Za-z]", 12345, [random.choice(string.ascii_letters + string.digits) for _ in range(40)]),
    (50, r"[^0-9A-Za-z]", 12345, [random.choice(string.punctuation) for _ in range(50)]),
])
def test_task_func(n, pattern, seed, expected_matches):
    random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, rand_str)
    assert matches == expected_matches