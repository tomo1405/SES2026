python
import numpy as np
import matplotlib.pyplot as plt
from src_0388 import task_func

def test_task_func():
    city_dict = {'New York': 8398748, 'London': 8900000, 'Beijing': 21516000, 'Tokyo': 13922147, 'Sydney': 5180000, 'Paris': 2240000, 'Berlin': 3671666, 'Moscow': 12444000, 'Madrid': 6451624, 'Rome': 2872000}
    city_population, ax = task_func(city_dict)
    assert city_population == {'New York': 8398748, 'London': 8900000, 'Beijing': 21516000, 'Tokyo': 13922147, 'Sydney': 5180000, 'Paris': 2240000, 'Berlin': 3671666, 'Moscow': 12444000, 'Madrid': 6451624, 'Rome': 2872000}
    assert isinstance(ax, plt.Axes)