import pandas as pd
import pytest
from src_0614 import task_func


def test_task_func():
    # Test with valid inputs
    goals = {'Team A': 10, 'Team B': 5, 'Team C': 0, 'Team D': -5, 'Team E': -10}
    penalties = {'Team A': 2, 'Team B': 1, 'Team C': 0, 'Team D': 3, 'Team E': 4}
    expected_scores = {'Team A': 8, 'Team B': 4, 'Team C': 0, 'Team D': -8, 'Team E': -14}
    expected_scores_df = pd.DataFrame(expected_scores, columns=['Team', 'Score'])
    expected_scores_df['Score'] = expected_scores_df['Score'].clip(*GOALS_RANGE)

    scores_df = task_func(goals, penalties)

    assert scores_df.equals(expected_scores_df)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        task_func({}, {})

    with pytest.raises(ValueError):
        task_func({'Team A': 10}, {'Team B': 5})

    with pytest.raises(ValueError):
        task_func({'Team A': 10, 'Team B': 5}, {'Team A': 2, 'Team B': 1})