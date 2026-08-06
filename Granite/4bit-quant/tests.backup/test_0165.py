import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from src_0165 import task_func

def test_task_func():
    fig = task_func()
    assert isinstance(fig, plt.Figure)

def test_task_func_with_custom_args():
    fig = task_func(num_labels=10, data_range=(0, 100))
    assert isinstance(fig, plt.Figure)