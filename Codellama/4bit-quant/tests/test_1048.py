import random
from datetime import datetime

import matplotlib.pyplot as plt


def test_task_func():
    date_str = "2023-02-28"
    date = datetime.strptime(date_str, "%Y-%m-%d")
    num_of_values = date.day
    random_values = [random.randint(1, 100) for _ in range(num_of_values)]
    _, ax = plt.subplots()
    ax.plot(random_values)
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Random Values"
    assert ax.get_title() == "Random Values vs Date"
    assert ax.get_xlim() == (0, num_of_values)
    assert ax.get_ylim() == (0, 100)
    assert ax.get_xticks() == [i for i in range(num_of_values)]
    assert ax.get_yticks() == [i for i in range(100)]
    assert ax.get_xticklabels() == [date.strftime("%Y-%m-%d") for i in range(num_of_values)]
    assert ax.get_yticklabels() == [str(i) for i in range(100)]