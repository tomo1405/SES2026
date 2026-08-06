python
import random
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from src_0232 import ValueObject

class TestTaskFunc:
    def test_empty_list(self):
        obj_list = []
        ax = task_func(obj_list)
        assert isinstance(ax, Axes)
        assert ax.get_title() == "Fit results: mu = 0.00,  std = 0.00"

    def test_single_value(self):
        obj_list = [ValueObject(mu=10, std=2)]
        ax = task_func(obj_list)
        assert isinstance(ax, Axes)
        assert ax.get_title() == "Fit results: mu = 10.00,  std = 2.00"

    def test_multiple_values(self):
        obj_list = [ValueObject(mu=10, std=2), ValueObject(mu=20, std=3), ValueObject(mu=30, std=4)]
        ax = task_func(obj_list)
        assert isinstance(ax, Axes)
        assert ax.get_title() == "Fit results: mu = 20.00,  std = 2.41"