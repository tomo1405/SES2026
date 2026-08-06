import pytest
from src_0419 import task_func

def test_task_func():
    # Assuming X and Y are defined and valid inputs for the function
    X = ...  # Replace with actual data or placeholder
    Y = ...  # Replace with actual data or placeholder

    model, ax = task_func(X, Y)

    # Add assertions or checks to validate the output
    assert model is not None, "Model should be returned"
    assert ax is not None, "Axes object should be returned"
    assert ax.get_title() == 'ROC curve', "Title should be 'ROC curve'"
    assert len(ax.lines) > 0, "Plot should have at least one line"