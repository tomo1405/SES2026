python
import requests
import pandas as pd
import pytest

def task_func(api_url):
    # Send the GET request and handle API failure
    if not isinstance(api_url, str):
        raise TypeError("api_url must be a string")

    response = requests.get(api_url, timeout=5)
    response.raise_for_status()

    # Parse the JSON response and convert it to a pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Generate a plot if the DataFrame is not empty
    plot = df.plot() if not df.empty else None

    return df, plot

def test_task_func():
    # Test with valid API URL
    df, plot = task_func("https://jsonplaceholder.typicode.com/todos/1")
    assert isinstance(df, pd.DataFrame)
    assert plot is None

    # Test with invalid API URL
    with pytest.raises(requests.exceptions.RequestException):
        task_func("https://invalid_url.com")

    # Test with invalid API response
    with pytest.raises(ValueError):
        task_func("https://jsonplaceholder.typicode.com/todos/1000")

    # Test with invalid API response data
    with pytest.raises(TypeError):
        task_func("https://jsonplaceholder.typicode.com/todos/1001")