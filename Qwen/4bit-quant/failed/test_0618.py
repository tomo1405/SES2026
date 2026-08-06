import pytest
from src_0618 import task_func

def test_task_func_no_rng_seed():
    result_df = task_func(goals=5, penalties=3)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == len(task_func.TEAMS)
    assert all(isinstance(row[0], str) for row in result_df.values)
    assert all(isinstance(row[1], str) for row in result_df.values)

def test_task_func_with_rng_seed():
    result_df1 = task_func(goals=5, penalties=3, rng_seed=42)
    result_df2 = task_func(goals=5, penalties=3, rng_seed=42)
    assert result_df1.equals(result_df2)

def test_task_func_column_names():
    result_df = task_func(goals=5, penalties=3)
    assert 'Team' in result_df.columns
    assert 'Match Result' in result_df.columns
    assert 'Goals' in result_df.columns
    assert 'Penalty Cost' in result_df.columns

def test_task_func_extracted_values():
    result_df = task_func(goals=5, penalties=3, rng_seed=42)
    for _, row in result_df.iterrows():
        goals_match = re.search(r'\((\d+) goals', row['Match Result'])
        penalty_cost_match = re.search(r'\$(\d+)', row['Match Result'])
        assert goals_match and int(goals_match.group(1)) == row['Goals']
        assert penalty_cost_match and int(penalty_cost_match.group(1)) == row['Penalty Cost']

def test_task_func_empty_teams():
    result_df = task_func(goals=5, penalties=3, teams=[])
    assert result_df.empty

def test_task_func_negative_goals():
    with pytest.raises(ValueError):
        task_func(goals=-1, penalties=3)

def test_task_func_negative_penalties():
    with pytest.raises(ValueError):
        task_func(goals=5, penalties=-1)