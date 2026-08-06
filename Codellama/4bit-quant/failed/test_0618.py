import pytest
from src_0618 import task_func

# Test 1: Test that the function returns a DataFrame with the correct columns
def test_return_type():
    goals = 10
    penalties = 5
    rng_seed = 1234
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    results_df = task_func(goals, penalties, rng_seed, teams)
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.columns.tolist() == ['Team', 'Match Result', 'Goals', 'Penalty Cost']

# Test 2: Test that the function returns the correct number of rows
def test_num_rows():
    goals = 10
    penalties = 5
    rng_seed = 1234
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    results_df = task_func(goals, penalties, rng_seed, teams)
    assert len(results_df) == len(teams)

# Test 3: Test that the function returns the correct number of goals and penalty costs
def test_goals_penalty_cost():
    goals = 10
    penalties = 5
    rng_seed = 1234
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    results_df = task_func(goals, penalties, rng_seed, teams)
    assert results_df['Goals'].sum() == goals * len(teams)
    assert results_df['Penalty Cost'].sum() == penalties * len(teams)

# Test 4: Test that the function returns the correct match results
def test_match_results():
    goals = 10
    penalties = 5
    rng_seed = 1234
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    results_df = task_func(goals, penalties, rng_seed, teams)
    expected_results = [
        ['Team A', '(0 goals, $0)'],
        ['Team B', '(0 goals, $0)'],
        ['Team C', '(0 goals, $0)'],
        ['Team D', '(0 goals, $0)'],
        ['Team E', '(0 goals, $0)']
    ]
    assert results_df.to_dict('records') == expected_results

# Test 5: Test that the function returns the correct visualization
def test_visualization():
    goals = 10
    penalties = 5
    rng_seed = 1234
    teams = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    results_df = task_func(goals, penalties, rng_seed, teams)
    ax = results_df.set_index('Team')[['Goals', 'Penalty Cost']].plot(kind='bar', stacked=True)
    plt.ylabel('Counts')
    plt.title('Football Match Results Analysis')
    plt.tight_layout()
    plt.show()
    assert ax.get_title() == 'Football Match Results Analysis'
    assert ax.get_ylabel() == 'Counts'
    assert ax.get_xlabel() == 'Team'
    assert ax.get_legend() == ['Goals', 'Penalty Cost']