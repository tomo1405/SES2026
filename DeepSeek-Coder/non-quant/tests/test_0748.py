import pytest
from src_0748 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    assert task_func("The numbers are 1.2 and 3.45") == (2, 4.65)
    
    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()