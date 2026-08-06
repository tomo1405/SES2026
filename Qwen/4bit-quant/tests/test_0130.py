import pytest
from src_0130 import task_func
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Mocking the requests.get function to simulate responses
class MockResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP error occurred with status code: {self.status_code}")

def test_task_func_with_valid_table():
    # Simulate a valid HTML page with a table
    html_content = """
    <html>
        <body>
            <table>
                <thead>
                    <tr><th>Name</th><th>Age</th></tr>
                </thead>
                <tbody>
                    <tr><td>John Doe</td><td>30</td></tr>
                    <tr><td>Jane Smith</td><td>25</td></tr>
                </tbody>
            </table>
        </body>
    </html>
    """
    mock_response = MockResponse(200, html_content)
    with pytest.raises(requests.HTTPError):
        # Simulate an HTTP error
        task_func()

    # Patch the requests.get method to return the mock response
    with requests_mock.Mocker() as m:
        m.get('http://example.com', text=html_content)
        df = task_func()
        assert isinstance(df, pd.DataFrame)
        assert df.equals(pd.DataFrame({
            'Name': ['John Doe', 'Jane Smith'],
            'Age': ['30', '25']
        }))

def test_task_func_no_table():
    # Simulate a page without a table
    html_content = """
    <html>
        <body>
            <h1>No Table Here</h1>
        </body>
    </html>
    """
    mock_response = MockResponse(200, html_content)
    with pytest.raises(ValueError) as excinfo:
        task_func()
    assert str(excinfo.value) == "No table found on the page."

def test_task_func_empty_table():
    # Simulate a page with an empty table
    html_content = """
    <html>
        <body>
            <table>
                <thead>
                    <tr><th>Name</th><th>Age</th></tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        </body>
    </html>
    """
    mock_response = MockResponse(200, html_content)
    with pytest.raises(ValueError) as excinfo:
        task_func()
    assert str(excinfo.value) == "No data found in the table."

def test_task_func_connection_error():
    # Simulate a connection error
    with pytest.raises(ConnectionError) as excinfo:
        task_func()
    assert str(excinfo.value) == "Could not connect to URL: None"