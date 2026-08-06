import pytest
from src_1015 import task_func

def test_task_func():
    # Test case 1: api_url is a string
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    df, plot = task_func(api_url)
    assert isinstance(df, pd.DataFrame)
    assert plot is not None

    # Test case 2: api_url is not a string
    with pytest.raises(TypeError):
        api_url = 123
        task_func(api_url)

    # Test case 3: api_url is a string but not a valid URL
    with pytest.raises(requests.exceptions.RequestException):
        api_url = "not_a_valid_url"
        task_func(api_url)