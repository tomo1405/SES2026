import pytest
from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    counter = Counter(flat_list)
    df = pd.DataFrame.from_dict(counter, orient='index', columns=['Count'])
    df.index.name = 'MenuItem'
    return df

def test_task_func():
    list_of_menuitems = [['Pizza', 'Pasta'], ['Pizza', 'Salad'], ['Pasta', 'Salad']]
    expected_df = pd.DataFrame({'Count': [3, 2, 2]}, index=pd.Index(['Pizza', 'Pasta', 'Salad'], name='MenuItem'))
    actual_df = task_func(list_of_menuitems)
    assert actual_df.equals(expected_df)

if __name__ == '__main__':
    pytest.main()