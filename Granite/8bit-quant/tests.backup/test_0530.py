import pytest
from src_0530 import task_func

def test_task_func():
    num_rolls = 100
    num_dice = 2
    random_seed = 0
    plot_path = "test_plot.png"

    sums_counter, ax = task_func(num_rolls, num_dice, plot_path, random_seed)

    assert isinstance(sums_counter, dict)
    assert isinstance(ax, object)

    assert len(sums_counter) == 6  # There are 6 possible sums of rolling 2 dice (2-6)
    assert ax.get_xlabel() == "Sum of Dice Roll"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Distribution of Dice Roll Sums"

if __name__ == "__main__":
    pytest.main()