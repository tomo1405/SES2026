import pytest
from src_0211 import task_func
import matplotlib.pyplot as plt

def test_task_func_with_no_data():
    data = []
    ax = task_func(data)
    assert len(ax.patches) == 0, "No bars should be present for empty data"
    assert ax.get_xlabel() == 'Letter'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Letter Counts with Max Value Letter Highlighted'

def test_task_func_with_single_entry():
    data = [('a', 1)]
    ax = task_func(data)
    assert len(ax.patches) == 1, "One bar should be present for single entry"
    assert ax.patches[0].get_height() == 1
    assert ax.patches[0].get_color() == 'blue'  # Default color for non-max value letter
    assert ax.get_legend().get_texts()[0].get_text() == 'Letter Counts'
    assert ax.get_legend().get_texts()[1].get_text() == 'Max Value Letter'

def test_task_func_with_multiple_entries():
    data = [('a', 1), ('b', 2), ('c', 3), ('a', 4)]
    ax = task_func(data)
    assert len(ax.patches) == 3, "Three bars should be present for multiple entries"
    assert ax.patches[0].get_height() == 2  # 'a' appears twice, total count is 5
    assert ax.patches[1].get_height() == 2
    assert ax.patches[2].get_height() == 3
    assert ax.patches[0].get_color() == 'red'  # 'a' has the max value
    assert ax.get_legend().get_texts()[0].get_text() == 'Letter Counts'
    assert ax.get_legend().get_texts()[1].get_text() == 'Max Value Letter'

def test_task_func_with_max_value_letter_not_in_data():
    data = [('x', 1), ('y', 2), ('z', 3)]
    ax = task_func(data)
    assert len(ax.patches) == 3, "Three bars should be present"
    assert ax.patches[0].get_color() == 'blue'
    assert ax.patches[1].get_color() == 'blue'
    assert ax.patches[2].get_color() == 'blue'
    assert ax.get_legend().get_texts()[0].get_text() == 'Letter Counts'
    assert ax.get_legend().get_texts()[1].get_text() == 'Max Value Letter'

def test_task_func_with_identical_values():
    data = [('a', 1), ('b', 1), ('c', 1)]
    ax = task_func(data)
    assert len(ax.patches) == 3, "Three bars should be present"
    assert all(patch.get_height() == 1 for patch in ax.patches)
    assert all(patch.get_color() == 'blue' for patch in ax.patches)
    assert ax.get_legend().get_texts()[0].get_text() == 'Letter Counts'
    assert ax.get_legend().get_texts()[1].get_text() == 'Max Value Letter'

# Run the tests
if __name__ == "__main__":
    pytest.main()