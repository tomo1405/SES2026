import pytest
from src_0143 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    fig, axs = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(axs, np.ndarray)
    assert len(axs) == 2
    assert axs[0].get_title() == 'Sine function'
    assert axs[0].get_xlabel() == 'x'
    assert axs[0].get_ylabel() == 'sin(x)'
    assert axs[1].get_title() == 'Cosine function'
    assert axs[1].get_xlabel() == 'x'
    assert axs[1].get_ylabel() == 'cos(x)'
    plt.close(fig)