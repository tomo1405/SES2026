import matplotlib.pyplot as plt
import pandas as pd


def test_task_func():
    data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]}
    column = 'A'
    df = pd.DataFrame(data)
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    counts = df[column].value_counts()
    missing_categories = list(set(CATEGORIES) - set(counts.index))
    for category in missing_categories:
        counts[category] = 0
    counts = counts.reindex(CATEGORIES)
    ax = counts.plot(kind='bar')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    plt.show()
    assert ax.get_xlabel() == 'Category'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == f'Distribution of {column}'
    assert ax.get_legend() == None
    assert ax.get_xaxis().get_ticklabels() == ['A', 'B', 'C', 'D', 'E']
    assert ax.get_yaxis().get_ticklabels() == [0, 1, 2, 3, 4, 5]