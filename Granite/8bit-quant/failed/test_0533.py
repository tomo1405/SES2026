import pytest
from src_0533 import task_func

def test_task_func():
    # Test case 1: Check if duplicates_counter is calculated correctly for a dataframe with duplicates
    df1 = pd.DataFrame({"value": [1, 2, 3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]})
    duplicates_counter1, ax1 = task_func(df1)
    assert duplicates_counter1 == Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1})

    # Test case 2: Check if mu and std are calculated correctly for a dataframe without duplicates
    df2 = pd.DataFrame({"value": [1, 2, 3, 4, 5]})
    duplicates_counter2, ax2 = task_func(df2)
    assert ax2.lines[0].get_ydata().sum() == 1.0  # Check if the area under the curve is 1.0

    # Test case 3: Check if ax.set_xlabel(), ax.set_ylabel(), and ax.set_title() are called correctly
    df3 = pd.DataFrame({"value": [1, 2, 3, 4, 5]})
    duplicates_counter3, ax3 = task_func(df3)
    assert ax3.get_xlabel() == "Value"
    assert ax3.get_ylabel() == "Frequency"
    assert ax3.get_title() == "Distribution"