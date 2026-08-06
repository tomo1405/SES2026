import re
import math
from src_0748 import task_func
def test_task_func():
    s = "There are 3 numbers: 1, 2, 3. Their squares are 1, 4, 9."
    count, sqrt_sum = task_func(s)
    assert count == 3
    assert sqrt_sum == math.sqrt(1) + math.sqrt(4) + math.sqrt(9)
    s = "There are 2 numbers: 2.5, 5. Their squares are 6.25, 25."
    count, sqrt_sum = task_func(s)
    assert count == 2
    assert sqrt_sum == math.sqrt(2.5) + math.sqrt(5)
    s = "There are no numbers."
    count, sqrt_sum = task_func(s)
    assert count == 0
    assert sqrt_sum == 0