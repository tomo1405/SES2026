import pytest
from src_0130 import task_func
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Mocking the requests module
class MockResponse:
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"HTTP error occurred: {self.status_code}")

def mock_requests_get(url):
    if url == 'http://example.com':
        return MockResponse(200, """
        <html>
            <body>
                <table>
                    <tr><th>Name</th><th>Age</th></tr>
                    <tr><td>John Doe</td><td>30</td></tr>
                    <tr><td>Jane Smith</td><td>25</td></tr>
                </table>
            </body>
        </html>
        """)
    elif url == 'http://no-table.com':
        return MockResponse(200, "<html><body>No table here</body></html>")
    elif url == 'http://no-data.com':
        return MockResponse(200, """
        <html>
            <body>
                <table>
                    <tr><th>Name</th><th>Age</th></tr>
                </table>
            </body>
        </html>
        """)
    elif url == 'http://connection-error.com':
        raise requests.ConnectionError("Connection error")
    elif url == 'http://http-error.com':
        return MockResponse(404, "Not Found")

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_success():
    df = task_func('http://example.com')
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Name', 'Age']
    assert len(df) == 2
    assert df.iloc[0]['Name'] == 'John Doe'
    assert df.iloc[0]['Age'] == '30'

def test_task_func_no_table():
    with pytest.raises(ValueError, match="No table found on the page."):
        task_func('http://no-table.com')

def test_task_func_no_data():
    with pytest.raises(ValueError, match="No data found in the table."):
        task_func('http://no-data.com')

def test_task_func_connection_error():
    with pytest.raises(ConnectionError, match="Could not connect to URL: Connection error"):
        task_func('http://connection-error.com')

def test_task_func_http_error():
    with pytest.raises(requests.HTTPError, match="HTTP error occurred: 404"):
        task_func('http://http-error.com')