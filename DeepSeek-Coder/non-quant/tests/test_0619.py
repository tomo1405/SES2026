import pytest
from src_0619 import task_func

def test_task_func():
    # Test the function with different inputs
    results, plots = task_func(goals=5, penalties=3)
    
    # Add assertions to verify the output
    assert isinstance(results, pd.DataFrame), "The results should be a DataFrame"
    assert len(plots) == 2, "There should be two plots"
    assert all(isinstance(plot, plt.Figure) for plot in plots), "Plots should be matplotlib figures"