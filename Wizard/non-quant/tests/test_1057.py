python
import pytest
import numpy as np
import random
import matplotlib.pyplot as plt
from src_1057 import task_func

def test_task_func():
    # Test case 1: n_pairs = 26
    bars = task_func(26)
    assert len(bars) == 26
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)
    assert all(bar.get_height() in range(1, 10) for bar in bars)
    assert all(bar.get_label() in ["a:1", "b:2", "c:3", "d:4", "e:5", "f:6", "g:7", "h:8", "i:9", "j:10", "k:11", "l:12", "m:13", "n:14", "o:15", "p:16", "q:17", "r:18", "s:19", "t:20", "u:21", "v:22", "w:23", "x:24", "y:25", "z:26"] for bar in bars)

    # Test case 2: n_pairs = 13
    bars = task_func(13)
    assert len(bars) == 13
    assert all(isinstance(bar, plt.Rectangle) for bar in bars)
    assert all(bar.get_height() in range(1, 10) for bar in bars)
    assert all(bar.get_label() in ["a:1", "b:2", "c:3", "d:4", "e:5", "f:6", "g:7", "h:8", "i:9", "j:10", "k:11", "l:12", "m:13"] for bar in bars)

    # Test case 3: n_pairs = 0
    with pytest.raises(ValueError):
        task_func(0)

    # Test case 4: n_pairs = 27
    with pytest.raises(ValueError):
        task_func(27)

    # Test case 5: n_pairs = 100
    with pytest.raises(ValueError):
        task_func(100)