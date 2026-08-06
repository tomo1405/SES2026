import pytest
from src_0211 import task_func
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple dataset
    data = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
    ax = task_func(data)
    
    # Check if the correct number of bars are plotted
    assert len(ax.patches) == 3  # 'a', 'b', 'c'
    
    # Check if the max value letter is highlighted
    max_value_letter = 'c'
    max_value_count = 4
    for bar in ax.patches:
        if bar.get_x() == list(ax.get_xticks()).index(max_value_letter):
            assert bar.get_height() == max_value_count
            assert bar.get_color() == 'red'
            break
    else:
        pytest.fail("Max value letter not highlighted correctly")

    # Check if labels and title are set correctly
    assert ax.get_xlabel() == 'Letter'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Letter Counts with Max Value Letter Highlighted'

    # Check if legend is present
    assert ax.get_legend() is not None

# Clean up after tests
@pytest.fixture(autouse=True)
def cleanup():
    plt.close('all')