python
import csv
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from src_1055 import task_func

def test_task_func():
    file_path = "data.csv"
    population = [1, 2, 3, 4, 5]
    with open(file_path, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows([[i] for i in population])

    mean, std_dev, ax = task_func(file_path)

    assert isinstance(mean, float)
    assert isinstance(std_dev, float)
    assert isinstance(ax, plt.Axes)