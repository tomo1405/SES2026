python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    analyzed_df = analyzed_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
    ax = sns.heatmap(analyzed_df, annot=True)
    plt.show()
    return analyzed_df, ax

# Test cases
def test_task_func_valid_input():
    data = [
        ['A', 'B', 1],
        ['A', 'C', 2],
        ['B', 'C', 3],
        ['B', 'D', 4],
        ['C', 'D', 5],
        ['C', 'E', 6],
        ['D', 'E', 7],
        ['D', 'F', 8],
        ['E', 'F', 9],
        ['E', 'G', 10]
    ]
    analyzed_df, ax = task_func(data)
    assert isinstance(analyzed_df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.AxesGrid)

def test_task_func_invalid_input():
    data = [
        ['A', 'B', 1],
        ['A', 'C', 2],
        ['B', 'C', 3],
        ['B', 'D', 4],
        ['C', 'D', 5],
        ['C', 'E', 6],
        ['D', 'E', 7],
        ['D', 'F', 8],
        ['E', 'F', 9],
        ['E', 'G', 10]
    ]
    analyzed_df, ax = task_func(data)
    assert isinstance(analyzed_df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.AxesGrid)