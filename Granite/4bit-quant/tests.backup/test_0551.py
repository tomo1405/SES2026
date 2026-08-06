import pytest
from collections import Counter
import pandas as pd

def task_func(list_of_menuitems):
    # Flattening the list using list comprehension
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    counter = Counter(flat_list)

    # Creating the DataFrame
    df = pd.DataFrame.from_dict(counter, orient='index', columns=['Count'])
    df.index.name = 'MenuItem'

    return df

def test_task_func():
    list_of_menuitems = [['item1', 'item2', 'item3'], ['item2', 'item3', 'item4'], ['item3', 'item4', 'item5']]
    expected_df = pd.DataFrame({'Count': [3, 3, 3]}, index=pd.Index(['item1', 'item2', 'item3', 'item4', 'item5'], name='MenuItem'))
    actual_df = task_func(list_of_menuitems)
    assert actual_df.equals(expected_df)

if __name__ == '__main__':
    pytest.main()