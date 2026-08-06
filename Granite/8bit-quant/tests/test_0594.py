import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
from src_0594 import task_func

def test_task_func():
    hours = 10
    file_path, ax = task_func(hours)
    assert os.path.exists(file_path)
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_output_dir():
    hours = 10
    output_dir = './custom_output'
    file_path, ax = task_func(hours, output_dir)
    assert os.path.exists(file_path)
    assert ax is not None
    assert isinstance(ax, plt.Axes)
    assert file_path.startswith(output_dir)

def test_task_func_with_zero_hours():
    hours = 0
    file_path, ax = task_func(hours)
    assert file_path is None
    assert ax is None