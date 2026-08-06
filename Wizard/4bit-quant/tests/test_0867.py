python
import numpy as np
import pytest
from src_0867 import task_func

def test_task_func():
    data = [('item1', 1, 2), ('item2', 3, 4), ('item3', 5, 6)]
    labels = task_func(data)
    assert len(labels) == 3
    assert labels[0] == labels[1] or labels[0] == labels[2] or labels[1] == labels[2]