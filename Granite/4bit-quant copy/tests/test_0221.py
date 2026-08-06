import pytest
from src_0221 import task_func

def test_task_func():
    colors = ['red', 'blue', 'green', 'yellow']
    expected_output = ' turtle graphics output with 4 squares of different colors'

    # Mock the choice function to make the test deterministic
    def mock_choice(sequence):
        return sequence[0]
    with pytest.patch('random.choice', side_effect=mock_choice):
        result = task_func(colors)

    assert result == expected_output