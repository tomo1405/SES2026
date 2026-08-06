import pytest
from src_0193 import task_func

def test_task_func():
    # Test case 1: Test with default arguments
    names = task_func()
    assert names == ["Josie Smith", "Mugsy Dog Smith"]
    
    # Test case 2: Test with custom arguments
    names = task_func(text="John Doe [123 Main St, Anytown, USA]", email_address="john.doe@example.com", email_password="password123")
    assert names == ["John Doe"]
    
    # Test case 3: Test with invalid email address and password
    with pytest.raises(smtplib.SMTPAuthenticationError):
        names = task_func(email_address="invalid.email@gmail.com", email_password="wrongpassword")