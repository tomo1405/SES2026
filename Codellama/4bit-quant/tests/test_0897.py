from typing import Counter

from src_0897 import task_func


def test_task_func():
    # Test case 1: length = 1, count = 1, seed = 0
    length = 1
    count = 1
    seed = 0
    expected_result = Counter({'a': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 2: length = 2, count = 2, seed = 0
    length = 2
    count = 2
    seed = 0
    expected_result = Counter({'aa': 1, 'ab': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 3: length = 3, count = 3, seed = 0
    length = 3
    count = 3
    seed = 0
    expected_result = Counter({'aaa': 1, 'aab': 1, 'aba': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 4: length = 4, count = 4, seed = 0
    length = 4
    count = 4
    seed = 0
    expected_result = Counter({'aaaa': 1, 'aaab': 1, 'aaba': 1, 'abaa': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 5: length = 5, count = 5, seed = 0
    length = 5
    count = 5
    seed = 0
    expected_result = Counter({'aaaaa': 1, 'aaaab': 1, 'aaaba': 1, 'aabaa': 1, 'abaaa': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 6: length = 6, count = 6, seed = 0
    length = 6
    count = 6
    seed = 0
    expected_result = Counter({'aaaaaa': 1, 'aaaaba': 1, 'aaabaa': 1, 'aabaab': 1, 'abaaab': 1, 'baaaaa': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 7: length = 7, count = 7, seed = 0
    length = 7
    count = 7
    seed = 0
    expected_result = Counter({'aaaaaaa': 1, 'aaaabaa': 1, 'aaabaab': 1, 'aabaaba': 1, 'abaaaba': 1, 'baaaaab': 1, 'aaaaaab': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 8: length = 8, count = 8, seed = 0
    length = 8
    count = 8
    seed = 0
    expected_result = Counter({'aaaaaaaa': 1, 'aaaabaab': 1, 'aaabaaba': 1, 'aabaabaa': 1, 'abaaabaa': 1, 'baaaabaa': 1, 'aaaaaaba': 1, 'aaaaabaa': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 9: length = 9, count = 9, seed = 0
    length = 9
    count = 9
    seed = 0
    expected_result = Counter({'aaaaaaaaa': 1, 'aaaabaaba': 1, 'aaabaabaa': 1, 'aabaabaab': 1, 'abaaabaab': 1, 'baaaabaab': 1, 'aaaaaabaa': 1, 'aaaaabaab': 1, 'aaaaaabaa': 1})
    assert task_func(length, count, seed) == expected_result

    # Test case 10: length = 10, count = 10, seed = 0
    length = 10
    count = 10
    seed = 0
    expected_result = Counter({'aaaaaaaaaa': 1, 'aaaabaabaa': 1, 'aaabaabaab': 1, 'aabaabaaba': 1, 'abaaabaaba': 1, 'baaaabaaba': 1, 'aaaaaabaab': 1, 'aaaaabaaba': 1, 'aaaaaabaab': 1, 'aaaaabaaba': 1})
    assert task_func(length, count, seed) == expected_result