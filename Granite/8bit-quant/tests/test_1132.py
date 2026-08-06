from unittest.mock import Mock

import pytest
from src_1132 import task_func


def test_task_func():
    # Mock the cursor object
    cursor = Mock()

    # Test case 1: salt is not a string
    with pytest.raises(TypeError):
        task_func(123, cursor)

    # Test case 2: salt is a string, but not a valid salt
    with pytest.raises(TypeError):
        task_func("not a salt", cursor)

    # Test case 3: valid salt, no users to update
    salt = "abc123"
    cursor.execute.return_value = None
    assert task_func(salt, cursor) == 0

    # Test case 4: valid salt, update one user
    salt = "abc123"
    cursor.execute.side_effect = [
        [("id1", "password1")],  # First execute to fetch users
        None,  # Second execute to update user
    ]
    assert task_func(salt, cursor) == 1