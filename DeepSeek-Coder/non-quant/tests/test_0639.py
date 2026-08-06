import pytest
from src_0639 import task_func

def test_task_func():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (5, 100), "The DataFrame should have the correct shape"
    assert all(result.index == ['Team1', 'Team2', 'Team3', 'Team4', 'Team5']), "The index should be the teams"
    assert all(result.columns == [f'Game{i}' for i in range(1, 101)]), "The columns should be the games"