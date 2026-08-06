import pytest
from src_0193 import task_func

def test_task_func():
    # Test case 1: Default arguments
    names = task_func()
    assert names == ["Josie Smith", "Mugsy Dog Smith"]
    
    # Test case 2: Custom arguments
    names = task_func(text="John Doe [123 Main St, Anytown, USA]",
                      smtp_server="smtp.example.com",
                      smtp_port=25,
                      email_address="john.doe@example.com",
                      email_password="password123",
                      recepient_address="names@example.com")
    assert names == ["John Doe"]
    
    # Test case 3: Invalid email address
    with pytest.raises(smtplib.SMTPException):
        names = task_func(email_address="invalid_email")