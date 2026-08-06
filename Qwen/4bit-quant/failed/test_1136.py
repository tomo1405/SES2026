import pytest
from src_1136 import task_func

# Mocking the requests module to simulate API responses
@pytest.fixture
def mock_requests_get(monkeypatch):
    def mock_get(url):
        class MockResponse:
            def __init__(self, text):
                self.text = text
            
            def json(self):
                return json.loads(self.text)
        
        # Simulate a response with two repositories
        if url == 'https://api.github.com/users/example_user/repos':
            return MockResponse('''
                [
                    {"name": "repo1", "created_at": "2020-01-01T00:00:00Z"},
                    {"name": "repo2", "created_at": "2019-12-01T00:00:00Z"}
                ]
            ''')
        else:
            raise Exception("Unexpected URL")
    
    monkeypatch.setattr(requests, 'get', mock_get)

def test_task_func(mock_requests_get):
    result = task_func('example_user')
    assert result == ['repo2', 'repo1'], "The repositories should be sorted by creation date"

def test_task_func_with_no_repos(mock_requests_get):
    # Simulate a response with no repositories
    mock_requests_get.monkeypatch.setattr(requests, 'get', lambda url: MockResponse('[]'))
    result = task_func('no_repos_user')
    assert result == [], "No repositories should be returned for a user with no repos"