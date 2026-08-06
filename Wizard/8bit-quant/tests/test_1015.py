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
    # Test case 1: Valid API URL
    df, plot = task_func("https://jsonplaceholder.typicode.com/todos/1")
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, type(None))

    # Test case 2: Invalid API URL
    with pytest.raises(TypeError):
        task_func(123)

    # Test case 3: Empty DataFrame
    df, plot = task_func("https://jsonplaceholder.typicode.com/todos/100")
    assert df.empty
    assert isinstance(plot, type(None))