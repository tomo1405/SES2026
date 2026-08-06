import pytest
from src_0083 import login, load_user

def test_login_form():
    form = login.LoginForm(username='test_user', password='password')
    assert form.validate()

def test_login_user():
    user = load_user('test_user')
    assert user is not None
    assert user.check_password('password')

def test_logout_user():
    user = load_user('test_user')
    assert user is not None
    assert user.check_password('password')
    login.logout()
    assert current_user.is_anonymous