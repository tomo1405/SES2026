python
import pytest
from src_0618 import task_func

def test_task_func():
    # Test case 1: Test with default parameters
    results_df = task_func(5, 3)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(x, str) for x in results_df['Team'])
    assert all(isinstance(x, str) for x in results_df['Match Result'])
    assert all(re.match(r'\((\d+) goals, \$(\d+)\)', x) for x in results_df['Match Result'])
    assert all(int(re.search(r'\((\d+) goals', x).group(1)) <= 5 for x in results_df['Match Result'])
    assert all(int(re.search(r'\$(\d+)', x).group(1)) <= 3000 for x in results_df['Match Result'])

    # Test case 2: Test with custom parameters
    results_df = task_func(7, 4, rng_seed=42)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == 5
    assert results_df.columns.tolist() == ['Team', 'Match Result']
    assert all(isinstance(x, str) for x in results_df['Team'])
    assert all(isinstance(x, str) for x in results_df['Match Result'])
    assert all(re.match(r'\((\d+) goals, \$(\d+)\)', x) for x in results_df['Match Result'])
    assert all(int(re.search(r'\((\d+) goals', x).group(1)) <= 7 for x in results_df['Match Result'])
    assert all(int(re.search(r'\$(\d+)', x).group(1)) <= 4000 for x in results_df['Match Result'])

    # Test case 3: Test with empty DataFrame
    results_df = task_func(0, 0)
    assert isinstance(results_df, pd.DataFrame)
    assert results_df.empty

    # Test case 4: Test with invalid parameters
    with pytest.raises(ValueError):
        task_func(-1, 0)
    with pytest.raises(ValueError):
        task_func(0, -1)
    with pytest.raises(ValueError):
        task_func(10, 10)