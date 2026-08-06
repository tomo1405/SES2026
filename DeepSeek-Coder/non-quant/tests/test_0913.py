import pytest
from src_0913 import task_func

# Test cases
def test_task_func():
    # Test case 1: Basic functionality
    assert task_func(['a', 'b', 'a'], 2) == {'a': 2, 'b': 2}
    
    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()