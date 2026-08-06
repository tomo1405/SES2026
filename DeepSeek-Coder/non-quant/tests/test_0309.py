import pytest
from src_0309 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert not result.empty, "The DataFrame should not be empty"
    assert set(result.columns) == set(FIELDS + ['Average Grade', 'Average']), "Columns are incorrect"
    assert all(result['Average Grade'] == result.mean(axis=1)), "Average grades are incorrect"
    assert all(result.loc['Average'] == result.mean()), "Averages are incorrect"