import pytest
import requests
from src_0579 import task_func


def test_task_func_valid_username():
    username = 'test_user'
    response = requests.get(URL + username)
    response.raise_for_status()
    user_data = response.json()
    normalized_user_data = task_func(username)
    assert normalized_user_data == user_data

def test_task_func_invalid_username():
    username = 'invalid_user'
    response = requests.get(URL + username)
    with pytest.raises(Exception) as e:
        task_func(username)
    assert str(e.value) == f"Failed to fetch user data for '{username}'. HTTP status: {response.status_code} - {response.reason}."