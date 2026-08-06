import random
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    from_user_values = [d['from_user'] for d in result if 'from_user' in d]
    color = random.choice(colors)
    plt.figure()
    sns.histplot(from_user_values, color=color)
    plt.show()
import pytest

def test_task_func():
    result = [
        {'from_user': 1, 'to_user': 2},
        {'from_user': 3, 'to_user': 4},
        {'from_user': 5, 'to_user': 6},
        {'from_user': 7, 'to_user': 8},
        {'from_user': 9, 'to_user': 10}
    ]
    task_func(result)
    assert plt.figure() is not None
    assert sns.histplot() is not None
    assert plt.show() is not None

if __name__ == "__main__":
    pytest.main()