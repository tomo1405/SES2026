import numpy as np
import math
import random
from random import uniform
from src_0697 import task_func

def test_task_func():
    assert task_func(1, 1) == [(0.7071067811865476, 0.7071067811865475)]
    assert task_func(2, 2) == [(-1.414213562373095, 1.4142135623730951), (1.414213562373095, -1.4142135623730951)]
    assert task_func(3, 3) == [(2.1213203435596424, -2.1213203435596424), (-2.1213203435596424, 2.1213203435596424), (0.0, 0.0)]