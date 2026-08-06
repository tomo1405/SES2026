import pytest
from src_0613 import task_func

# Test cases for the function
def test_task_func():
    # Test case 1: Basic functionality
    goals = {'Team A': 3, 'Team B': 2}
    penalties = {'Team A': 2, 'Team B': 1}
    expected_output = pd.DataFrame({
        'Team': ['Team A', 'Team B'],
        'Goals': [3, 2],
        'Penalties': [2, 1],
        'Penalties Cost': [200, 100],
        'Performance Score': [1, 1]
    })
    result = task_func(goals, penalties)
    pd.testing.assert_frame_equal(result, expected_output)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()