import matplotlib.pyplot as plt
from src_0063 import task_func


def test_task_func():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    task_func(result)
    assert plt.gcf().axes[0].get_xlabel() == 'from_user'
    assert plt.gcf().axes[0].get_ylabel() == 'Count'
    assert plt.gcf().axes[0].get_title() == 'Histogram of from_user'
    assert plt.gcf().axes[0].get_xlim() == (0, 3)
    assert plt.gcf().axes[0].get_ylim() == (0, 3)
    assert plt.gcf().axes[0].get_xticks() == [1, 2, 3]
    assert plt.gcf().axes[0].get_yticks() == [1, 2, 3]
    assert plt.gcf().axes[0].get_xticklabels() == ['1', '2', '3']
    assert plt.gcf().axes[0].get_yticklabels() == ['1', '2', '3']
    assert plt.gcf().axes[0].get_xticklabels()[0].get_color() == 'b'
    assert plt.gcf().axes[0].get_yticklabels()[0].get_color() == 'b'
    assert plt.gcf().axes[0].get_xticklabels()[1].get_color() == 'g'
    assert plt.gcf().axes[0].get_yticklabels()[1].get_color() == 'g'
    assert plt.gcf().axes[0].get_xticklabels()[2].get_color() == 'r'
    assert plt.gcf().axes[0].get_yticklabels()[2].get_color() == 'r'
    assert plt.gcf().axes[0].get_xticklabels()[3].get_color() == 'c'
    assert plt.gcf().axes[0].get_yticklabels()[3].get_color() == 'c'
    assert plt.gcf().axes[0].get_xticklabels()[4].get_color() == 'm'
    assert plt.gcf().axes[0].get_yticklabels()[4].get_color() == 'm'
    assert plt.gcf().axes[0].get_xticklabels()[5].get_color() == 'y'
    assert plt.gcf().axes[0].get_yticklabels()[5].get_color() == 'y'
    assert plt.gcf().axes[0].get_xticklabels()[6].get_color() == 'k'
    assert plt.gcf().axes[0].get_yticklabels()[6].get_color() == 'k'