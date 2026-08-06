import pytest
from src_0533 import task_func

def test_task_func():
    # Test case 1: Check if duplicates_counter is calculated correctly for a dataframe with duplicates
    df1 = pd.DataFrame({"value": [1, 2, 3, 4, 5, 2, 3, 4, 5, 2]})
    duplicates_counter1, ax1 = task_func(df1)
    assert duplicates_counter1 == Counter({2: 3, 3: 2, 4: 2, 5: 3})

    # Test case 2: Check if mu and std are calculated correctly for a non-empty dataframe with non-constant values
    df2 = pd.DataFrame({"value": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    duplicates_counter2, ax2 = task_func(df2)
    assert ax2.get_xlabel() == "Value"
    assert ax2.get_ylabel() == "Frequency"
    assert ax2.get_title() == "Distribution"

    # Test case 3: Check if None is returned for an empty dataframe or a dataframe with constant values
    df3 = pd.DataFrame({"value": [1, 1, 1, 1, 1])
    duplicates_counter3, ax3 = task_func(df3)
    assert duplicates_counter3 is None
    df4 = pd.DataFrame({"value": []})
    duplicates_counter4, ax4 = task_func(df4)
    assert duplicates_counter4 is None