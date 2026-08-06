import pytest
from src_0386 import task_func

@pytest.mark.parametrize("input, expected_output", [
    ({"Apple": 1, "Banana": 2, "Cherry": 3}, (Counter({'Apple': 1, 'Banana': 2, 'Cherry': 3}), <matplotlib.axes._subplots.Axes object at 0x7f225e612e50>)),
    ({"Apple": 1, "Orange": 2, "Pear": 3}, (Counter({'Apple': 1, 'Orange': 2, 'Pear': 3}), <matplotlib.axes._subplots.Axes object at 0x7f225e612e50>)),
    ({"Apple": 1, "Banana": 2, "Cherry": 3, "Date": 4}, (Counter({'Apple': 1, 'Banana': 2, 'Cherry': 3, 'Date': 4}), <matplotlib.axes._subplots.Axes object at 0x7f225e612e50>)),
])
def test_task_func(input, expected_output):
    result = task_func(input)
    assert result == expected_output