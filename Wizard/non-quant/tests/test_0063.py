python
import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    from_user_values = [d['from_user'] for d in result if 'from_user' in d]
    color = random.choice(colors)
    plt.figure()
    sns.histplot(from_user_values, color=color)
    plt.show()

def test_task_func():
    result = [{'from_user': 1}, {'from_user': 2}, {'from_user': 3}, {'from_user': 4}, {'from_user': 5}]
    task_func(result)

test_task_func()