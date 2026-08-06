import random

from src_1116 import task_func


def test_task_func():
    dict1 = {'ABC': 3, 'XYZ': 2}
    expected_output = ['ABC' + ''.join(random.choice(ascii_uppercase) for _ in range(5)) for _ in range(3)] + \
                      ['XYZ' + ''.join(random.choice(ascii_uppercase) for _ in range(5)) for _ in range(2)]
    
    actual_output = task_func(dict1)
    
    assert actual_output == expected_output