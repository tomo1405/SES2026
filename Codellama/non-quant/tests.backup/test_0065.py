import pytest
from src_0065 import task_func
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def test_task_func():
    data = [
        ['A', 'B', 'C'],
        ['A', 'B', 'D'],
        ['A', 'C', 'E'],
        ['B', 'C', 'F'],
        ['B', 'C', 'G'],
        ['B', 'D', 'H'],
        ['C', 'D', 'I'],
        ['C', 'D', 'J'],
        ['C', 'E', 'K'],
        ['D', 'E', 'L'],
        ['D', 'E', 'M'],
        ['D', 'F', 'N'],
        ['E', 'F', 'O'],
        ['E', 'F', 'P'],
        ['E', 'G', 'Q'],
        ['F', 'G', 'R'],
        ['F', 'G', 'S'],
        ['F', 'H', 'T'],
        ['G', 'H', 'U'],
        ['G', 'H', 'V'],
        ['G', 'I', 'W'],
        ['H', 'I', 'X'],
        ['H', 'I', 'Y'],
        ['I', 'J', 'Z'],
    ]
    expected_analyzed_df = pd.DataFrame(
        {
            'col1': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            'col2': ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
            'col3': ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
        }
    )
    expected_ax = sns.heatmap(expected_analyzed_df, annot=True)
    plt.show()
    analyzed_df, ax = task_func(data)
    assert analyzed_df.equals(expected_analyzed_df)
    assert ax.equals(expected_ax)