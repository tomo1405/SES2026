import pytest
from src_0077 import task_func
from django.http import HttpRequest, HttpResponse

@pytest.fixture
def request():
    return HttpRequest()

def test_task_func_success(request):
    session_expire_time = 3600
    response = task_func(request, session_expire_time)
    assert isinstance(response, HttpResponse)
    assert 'session_key' in response.cookies
    session_key = response.cookies['session_key'].value
    assert len(session_key) == 20
    assert any(char.isdigit() for char in session_key)
    assert any(char.isalpha() for char in session_key)

def test_task_func_invalid_session_key_length(request):
    session_expire_time = 3600
    with pytest.raises(ValueError) as excinfo:
        task_func(request, session_expire_time)
    assert "Session key should contain both letters and digits" in str(excinfo.value)

def test_task_func_no_digits(request):
    session_expire_time = 3600
    original_choices = random.choices
    def mock_choices(population, k):
        return ['a'] * k
    random.choices = mock_choices
    with pytest.raises(ValueError) as excinfo:
        task_func(request, session_expire_time)
    assert "Session key should contain both letters and digits" in str(excinfo.value)
    random.choices = original_choices

def test_task_func_no_letters(request):
    session_expire_time = 3600
    original_choices = random.choices
    def mock_choices(population, k):
        return ['1'] * k
    random.choices = mock_choices
    with pytest.raises(ValueError) as excinfo:
        task_func(request, session_expire_time)
    assert "Session key should contain both letters and digits" in str(excinfo.value)
    random.choices = original_choices