import pytest
from src_0130 import task_func
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Mocking the requests module
class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP error occurred: {self.status_code}")

def mock_requests_get(url):
    if url == 'http://example.com':
        html_content = """
        <html>
            <body>
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Age</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>John Doe</td>
                            <td>30</td>
                        </tr>
                        <tr>
                            <td>Jane Smith</td>
                            <td>25</td>
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
        """
        return MockResponse(html_content)
    else:
        raise requests.ConnectionError("Could not connect to URL")

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_success():
    url = 'http://example.com'
    df = task_func(url)
    expected_data = {
        'Name': ['John Doe', 'Jane Smith'],
        'Age': ['30', '25']
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(df, expected_df)

def test_task_func_no_table():
    html_content = """
    <html>
        <body>
            <!-- No table here -->
        </body>
    </html>
    """
    def mock_requests_get_no_table(url):
        return MockResponse(html_content)
    
    with pytest.raises(ValueError) as excinfo:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(requests, 'get', mock_requests_get_no_table)
            task_func('http://example.com')
    assert str(excinfo.value) == "No table found on the page."

def test_task_func_no_data_in_table():
    html_content = """
    <html>
        <body>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Age</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- No data rows here -->
                </tbody>
            </table>
        </body>
    </html>
    """
    def mock_requests_get_no_data(url):
        return MockResponse(html_content)
    
    with pytest.raises(ValueError) as excinfo:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(requests, 'get', mock_requests_get_no_data)
            task_func('http://example.com')
    assert str(excinfo.value) == "No data found in the table."

def test_task_func_connection_error():
    def mock_requests_get_connection_error(url):
        raise requests.ConnectionError("Could not connect to URL")
    
    with pytest.raises(ConnectionError) as excinfo:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(requests, 'get', mock_requests_get_connection_error)
            task_func('http://example.com')
    assert str(excinfo.value) == "Could not connect to URL: Could not connect to URL"

def test_task_func_http_error():
    def mock_requests_get_http_error(url):
        return MockResponse("", status_code=404)
    
    with pytest.raises(requests.HTTPError) as excinfo:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(requests, 'get', mock_requests_get_http_error)
            task_func('http://example.com')
    assert str(excinfo.value) == "HTTP error occurred: 404"