python
import pytest
from src_1115 import task_func

def test_task_func():
    # Test case 1
    dict1 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10]}
    assert task_func(dict1) == expected_output

    # Test case 2
    dict2 = {'EMP$$101': 0, 'EMP$$102': 0, 'MGR$$101': 0, 'EMP$$103': 0}
    expected_output = {}
    assert task_func(dict2) == expected_output

    # Test case 3
    dict3 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10]}
    assert task_func(dict3) == expected_output

    # Test case 4
    dict4 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10]}
    assert task_func(dict4) == expected_output

    # Test case 5
    dict5 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1, 'EMP$$106': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10], 'EMP$$106': [10]}
    assert task_func(dict5) == expected_output

    # Test case 6
    dict6 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1, 'EMP$$106': 1, 'EMP$$107': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10], 'EMP$$106': [10], 'EMP$$107': [10]}
    assert task_func(dict6) == expected_output

    # Test case 7
    dict7 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1, 'EMP$$106': 1, 'EMP$$107': 1, 'EMP$$108': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10], 'EMP$$106': [10], 'EMP$$107': [10], 'EMP$$108': [10]}
    assert task_func(dict7) == expected_output

    # Test case 8
    dict8 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1, 'EMP$$106': 1, 'EMP$$107': 1, 'EMP$$108': 1, 'EMP$$109': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10], 'EMP$$106': [10], 'EMP$$107': [10], 'EMP$$108': [10], 'EMP$$109': [10]}
    assert task_func(dict8) == expected_output

    # Test case 9
    dict9 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1, 'EMP$$106': 1, 'EMP$$107': 1, 'EMP$$108': 1, 'EMP$$109': 1, 'EMP$$110': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10], 'EMP$$106': [10], 'EMP$$107': [10], 'EMP$$108': [10], 'EMP$$109': [10], 'EMP$$110': [10]}
    assert task_func(dict9) == expected_output

    # Test case 10
    dict10 = {'EMP$$101': 2, 'EMP$$102': 3, 'MGR$$101': 1, 'EMP$$103': 1, 'EMP$$104': 1, 'EMP$$105': 1, 'EMP$$106': 1, 'EMP$$107': 1, 'EMP$$108': 1, 'EMP$$109': 1, 'EMP$$110': 1, 'EMP$$111': 1}
    expected_output = {'EMP$$101': [10, 10], 'EMP$$102': [10, 10, 10], 'MGR$$101': [10], 'EMP$$104': [10], 'EMP$$105': [10], 'EMP$$106': [10], 'EMP$$107': [10], 'EMP$$108': [10], 'EMP$$109': [10], 'EMP$$110': [10], 'EMP$$111': [10]}
    assert task_func(dict10) == expected_output