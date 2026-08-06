python
import pytest
from src_0618 import task_func

def test_task_func():
    # Test case 1: Normal case with no random seed
    results_df = task_func(5, 2)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(x, str) for x in results_df['Team'])
    assert all(isinstance(x, str) for x in results_df['Match Result'])
    assert all(re.match(r'\((\d+) goals, \$(\d+)\)', x) for x in results_df['Match Result'])
    assert all(int(re.search(r'\((\d+) goals', x).group(1)) <= 5 for x in results_df['Match Result'])
    assert all(int(re.search(r'\$(\d+)', x).group(1)) <= 2000 for x in results_df['Match Result'])

    # Test case 2: Normal case with random seed
    results_df = task_func(5, 2, rng_seed=42)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(x, str) for x in results_df['Team'])
    assert all(isinstance(x, str) for x in results_df['Match Result'])
    assert all(re.match(r'\((\d+) goals, \$(\d+)\)', x) for x in results_df['Match Result'])
    assert all(int(re.search(r'\((\d+) goals', x).group(1)) <= 5 for x in results_df['Match Result'])
    assert all(int(re.search(r'\$(\d+)', x).group(1)) <= 2000 for x in results_df['Match Result'])

    # Test case 3: Goals and penalties are zero
    results_df = task_func(0, 0)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(x, str) for x in results_df['Team'])
    assert all(isinstance(x, str) for x in results_df['Match Result'])
    assert all(re.match(r'\((\d+) goals, \$(\d+)\)', x) for x in results_df['Match Result'])
    assert all(int(re.search(r'\((\d+) goals', x).group(1)) == 0 for x in results_df['Match Result'])
    assert all(int(re.search(r'\$(\d+)', x).group(1)) == 0 for x in results_df['Match Result'])

    # Test case 4: Goals and penalties are negative
    with pytest.raises(ValueError):
        task_func(-1, -1)

    # Test case 5: Goals and penalties are too large
    with pytest.raises(ValueError):
        task_func(100, 100)

    # Test case 6: Teams is empty
    with pytest.raises(ValueError):
        task_func(5, 2, teams=[])

    # Test case 7: Teams is None
    with pytest.raises(ValueError):
        task_func(5, 2, teams=None)

    # Test case 8: Teams is not a list
    with pytest.raises(TypeError):
        task_func(5, 2, teams='Team A')

    # Test case 9: Teams has duplicates
    with pytest.raises(ValueError):
        task_func(5, 2, teams=['Team A', 'Team B', 'Team A'])

    # Test case 10: Teams has non-string elements
    with pytest.raises(TypeError):
        task_func(5, 2, teams=['Team A', 'Team B', 123])

    # Test case 11: Teams has non-unique elements
    with pytest.raises(ValueError):
        task_func(5, 2, teams=['Team A', 'Team B', 'Team A', 'Team C', 'Team B'])

    # Test case 12: Teams has too many elements
    with pytest.raises(ValueError):
        task_func(5, 2, teams=['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F'])

    # Test case 13: Teams has too few elements
    with pytest.raises(ValueError):
        task_func(5, 2, teams=['Team A', 'Team B'])

    # Test case 14: Teams has too many elements with random seed
    with pytest.raises(ValueError):
        task_func(5, 2, rng_seed=42, teams=['Team A', 'Team B', 'Team C', 'Team D', 'Team E', 'Team F'])

    # Test case 15: Teams has too few elements with random seed
    with pytest.raises(ValueError):
        task_func(5, 2, rng_seed=42, teams=['Team A', 'Team B'])

    # Test case 16: Teams has non-unique elements with random seed
    with pytest.raises(ValueError):
        task_func(5, 2, rng_seed=42, teams=['Team A', 'Team B', 'Team A', 'Team C', 'Team B'])

    # Test case 17: Teams has non-string elements with random seed
    with pytest.raises(TypeError):
        task_func(5, 2, rng_seed=42, teams=['Team A', 'Team B', 123])

    # Test case 18: Visualization is not tested directly in unit tests, but we can test it indirectly
    # by checking if the plot is created without errors
    results_df = task_func(5, 2)
    ax = results_df.set_index('Team')[['Goals', 'Penalty Cost']].plot(kind='bar', stacked=True)
    plt.ylabel('Counts')
    plt.title('Football Match Results Analysis')
    plt.tight_layout()
    plt.show()