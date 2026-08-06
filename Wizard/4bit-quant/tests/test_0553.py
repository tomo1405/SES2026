python
import collections
import itertools
import matplotlib.pyplot as plt
import pytest

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine lists
    combined = list(itertools.chain(a, b))
    # Count occurrences of each item
    counter = collections.Counter(combined)
    # Get counts for predefined items
    item_counts = [counter.get(item, 0) for item in items]

    # Create a bar plot
    fig, ax = plt.subplots()
    ax.bar(items, item_counts, color='skyblue')
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Item Frequency in Combined List')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for item labels

    return ax

def test_task_func():
    # Test case 1
    a = [1, 2, 3]
    b = [2, 3, 4]
    expected_counts = [2, 2]
    expected_ax = plt.bar(['apple', 'banana'], expected_counts, color='skyblue')
    expected_ax.set_xlabel('Items')
    expected_ax.set_ylabel('Frequency')
    expected_ax.set_title('Item Frequency in Combined List')
    expected_ax.set_xticks(['apple', 'banana'])
    expected_ax.set_xticklabels(['apple', 'banana'])
    expected_ax.set_ylim(0, 2)
    expected_ax.set_yticks([0, 1, 2])
    expected_ax.set_yticklabels(['0', '1', '2'])

    actual_ax = task_func(a, b)
    assert actual_ax == expected_ax

    # Test case 2
    a = [1, 2, 3]
    b = []
    expected_counts = [1, 0]
    expected_ax = plt.bar(['apple', 'banana'], expected_counts, color='skyblue')
    expected_ax.set_xlabel('Items')
    expected_ax.set_ylabel('Frequency')
    expected_ax.set_title('Item Frequency in Combined List')
    expected_ax.set_xticks(['apple', 'banana'])
    expected_ax.set_xticklabels(['apple', 'banana'])
    expected_ax.set_ylim(0, 1)
    expected_ax.set_yticks([0, 1])
    expected_ax.set_yticklabels(['0', '1'])

    actual_ax = task_func(a, b)
    assert actual_ax == expected_ax

    # Test case 3
    a = []
    b = [2, 3, 4]
    expected_counts = [0, 3]
    expected_ax = plt.bar(['apple', 'banana'], expected_counts, color='skyblue')
    expected_ax.set_xlabel('Items')
    expected_ax.set_ylabel('Frequency')
    expected_ax.set_title('Item Frequency in Combined List')
    expected_ax.set_xticks(['apple', 'banana'])
    expected_ax.set_xticklabels(['apple', 'banana'])
    expected_ax.set_ylim(0, 3)
    expected_ax.set_yticks([0, 1, 2, 3])
    expected_ax.set_yticklabels(['0', '1', '2', '3'])

    actual_ax = task_func(a, b)
    assert actual_ax == expected_ax

    # Test case 4
    a = []
    b = []
    expected_counts = [0, 0]
    expected_ax = plt.bar(['apple', 'banana'], expected_counts, color='skyblue')
    expected_ax.set_xlabel('Items')
    expected_ax.set_ylabel('Frequency')
    expected_ax.set_title('Item Frequency in Combined List')
    expected_ax.set_xticks(['apple', 'banana'])
    expected_ax.set_xticklabels(['apple', 'banana'])
    expected_ax.set_ylim(0, 0)
    expected_ax.set_yticks([])
    expected_ax.set_yticklabels([])

    actual_ax = task_func(a, b)
    assert actual_ax == expected_ax