python
import random
import matplotlib.pyplot as plt
import seaborn as sns
from src_0063 import task_func

def test_task_func():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}]
    task_func(result)
    assert plt.gca().get_title() == 'Histogram'
    assert plt.gca().get_xlabel() == 'Values'
    assert plt.gca().get_ylabel() == 'Frequency'
    assert plt.gca().get_xlim() == (0, 3)
    assert plt.gca().get_ylim() == (0, 3)
    assert plt.gca().patches[0].get_facecolor() == (0.12156862745098039, 0.4666666666666667, 0.7058823529411765, 1.0)