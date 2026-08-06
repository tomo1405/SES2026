import pytest
from src_1048 import task_func

def test_task_func():
    date_str = "2023-02-28"
    date = datetime.strptime(date_str, "%Y-%m-%d")
    num_of_values = date.day
    random_values = [random.randint(1, 100) for _ in range(num_of_values)]
    ax = task_func(date_str)
    assert ax.get_xlabel() == "Day"
    assert ax.get_ylabel() == "Random Values"
    assert ax.get_title() == "Random Values vs Day"
    assert ax.get_xlim() == (1, num_of_values)
    assert ax.get_ylim() == (1, 100)
    assert ax.get_xticks() == range(1, num_of_values + 1)
    assert ax.get_yticks() == range(1, 101)
    assert ax.get_xticklabels() == [str(i) for i in range(1, num_of_values + 1)]
    assert ax.get_yticklabels() == [str(i) for i in range(1, 101)]
    assert ax.get_lines()[0].get_data() == (range(1, num_of_values + 1), random_values)