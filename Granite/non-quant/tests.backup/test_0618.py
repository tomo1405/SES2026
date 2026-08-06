import pytest
from src_0618 import task_func

def test_task_func():
    goals = 5
    penalties = 3
    rng_seed = 42
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    expected_results_df = pd.DataFrame([
        ['Team A', '(3 goals, $3000)'],
        ['Team B', '(2 goals, $2000)'],
        ['Team C', '(4 goals, $4000)'],
        ['Team D', '(1 goals, $1000)'],
        ['Team E', '(5 goals, $5000)']
    ], columns=['Team', 'Match Result'])
    expected_results_df['Goals'] = expected_results_df['Match Result'].apply(lambda x: int(re.search(r'\((\d+) goals', x).group(1)))
    expected_results_df['Penalty Cost'] = expected_results_df['Match Result'].apply(lambda x: int(re.search(r'\$(\d+)', x).group(1)))

    results_df = task_func(goals, penalties, rng_seed, teams)

    assert results_df.equals(expected_results_df)

if __name__ == '__main__':
    pytest.main()