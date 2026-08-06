from typing import Counter

from src_0801 import task_func


def test_task_func():
    # Test case 1: No input file
    assert task_func({}, {}) == Counter({'goals': 0, 'penalties': 0})

    # Test case 2: Input file with data
    assert task_func({'Team A': 2, 'Team B': 1}, {'Team A': 1, 'Team B': 2}) == Counter({'goals': 3, 'penalties': 3})

    # Test case 3: Input file with data and additional teams
    assert task_func({'Team A': 2, 'Team B': 1, 'Team C': 3}, {'Team A': 1, 'Team B': 2, 'Team C': 0}) == Counter({'goals': 5, 'penalties': 3})

    # Test case 4: Input file with data and additional teams, with different penalties
    assert task_func({'Team A': 2, 'Team B': 1, 'Team C': 3}, {'Team A': 1, 'Team B': 2, 'Team C': 0}, {'Team A': 1, 'Team B': 2, 'Team C': 0}) == Counter({'goals': 5, 'penalties': 3})

    # Test case 5: Input file with data and additional teams, with different penalties and goals
    assert task_func({'Team A': 2, 'Team B': 1, 'Team C': 3}, {'Team A': 1, 'Team B': 2, 'Team C': 0}, {'Team A': 1, 'Team B': 2, 'Team C': 0}, {'Team A': 1, 'Team B': 2, 'Team C': 0}) == Counter({'goals': 5, 'penalties': 3})