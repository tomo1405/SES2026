python
import collections
import matplotlib.pyplot as plt
import pytest

def task_func(data):
    if not data:
        return None

    combined_dict = {}
    for d in data:
        for k, v in d.items():
            if v is None:
                continue
            elif v < 0:
                raise ValueError("Scores must be non-negative.")
            if k in combined_dict:
                combined_dict[k].append(v)
            else:
                combined_dict[k] = [v]

    avg_scores = {k: sum(v) / len(v) for k, v in combined_dict.items()}
    avg_scores = collections.OrderedDict(sorted(avg_scores.items()))
    labels, values = zip(*avg_scores.items())

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["red", "yellow", "green", "blue", "purple"])
    ax.set_title("Average Student Scores")
    ax.set_xlabel("Student")
    ax.set_ylabel("Average Score")

    return ax

def test_task_func():
    # Test case 1: Empty data
    data = []
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 2: Non-empty data with valid scores
    data = [
        {"Alice": 80, "Bob": 90, "Charlie": 70},
        {"Alice": 85, "Bob": 95, "Charlie": 75},
        {"Alice": 90, "Bob": 80, "Charlie": 80},
    ]
    ax = task_func(data)
    assert ax is not None

    # Test case 3: Non-empty data with invalid scores
    data = [
        {"Alice": 80, "Bob": 90, "Charlie": -70},
        {"Alice": 85, "Bob": 95, "Charlie": 75},
        {"Alice": 90, "Bob": 80, "Charlie": 80},
    ]
    with pytest.raises(ValueError):
        task_func(data)