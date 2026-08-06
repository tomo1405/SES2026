import pytest
from src_1120 import task_func

def test_task_func():
    password_length = 10
    salt = "salty"
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(password_length))
    password = codecs.encode(password, 'latin-1').decode('utf-8')
    salted_password = (password + salt).encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    
    assert task_func(password_length, salt) == hashed_password