import pytest
from src_0770 import task_func

def test_task_func():
    # Test case 1
    list_of_menuitems = [
        ['apple', 'banana', 'apple'],
        ['banana', 'apple', 'banana'],
        ['apple', 'banana', 'apple']
    ]
    assert task_func(list_of_menuitems) == 'apple'

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()