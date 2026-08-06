python
import numpy as np
import matplotlib.pyplot as plt
from src_0388 import task_func

def test_task_func():
    city_dict = {'A': 'New York', 'B': 'London', 'C': 'Beijing', 'D': 'Tokyo', 'E': 'Sydney', 'F': 'Paris', 'G': 'Berlin', 'H': 'Moscow', 'I': 'Madrid', 'J': 'Rome'}
    city_population, ax = task_func(city_dict, max_range=1000000, seed=0)
    assert city_population == {'New York': 1000000, 'London': 1000000, 'Beijing': 1000000, 'Tokyo': 1000000, 'Sydney': 1000000, 'Paris': 1000000, 'Berlin': 1000000, 'Moscow': 1000000, 'Madrid': 1000000, 'Rome': 1000000}
    assert ax.get_xlabel() == 'City'
    assert ax.get_ylabel() == 'Population'
    assert ax.get_title() == 'City Populations'