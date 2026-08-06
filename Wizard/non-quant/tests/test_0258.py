python
import numpy as np
import math
import pytest
from src_0258 import task_func

def test_task_func():
    fig, ax = plt.subplots()
    ax = task_func(ax, 1)
    assert ax.get_rlabel_position() == 45.0