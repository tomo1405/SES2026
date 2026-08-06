python
import pytest
from src_0619 import task_func

def test_task_func():
    results_df, plots = task_func(5, 3)
    assert isinstance(results_df, pd.DataFrame)
    assert isinstance(plots, list)
    assert len(plots) == 2
    assert all(isinstance(plot, sns.axisgrid.FacetGrid) for plot in plots)