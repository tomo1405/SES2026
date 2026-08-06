import pytest
from src_0618 import task_func

def test_task_func():
    goals = 5
    penalties = 3
    rng_seed = 42
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    expected_results = pd.DataFrame([
        ['Team A', '(3 goals, $3000)'],
        ['Team B', '(2 goals, $2000)'],
        ['Team C', '(4 goals, $4000)'],
        ['Team D', '(1 goals, $1000)'],
        ['Team E', '(5 goals, $5000)']
    ], columns=['Team', 'Match Result'])
    expected_results['Goals'] = expected_results['Match Result'].apply(lambda x: int(re.search(r'\((\d+) goals', x).group(1)))
    expected_results['Penalty Cost'] = expected_results['Match Result'].apply(lambda x: int(re.search(r'\$(\d+)', x).group(1)))
    actual_results = task_func(goals, penalties, rng_seed, teams)
    assert actual_results.equals(expected_results)

def test_task_func_with_empty_df():
    goals = 1
    penalties = 1
    rng_seed = None
    teams = ['Team A', 'Team B']
    expected_results = pd.DataFrame(columns=['Team', 'Match Result', 'Goals', 'Penalty Cost'])
    actual_results = task_func(goals, penalties, rng_seed, teams)
    assert actual_results.equals(expected_results)