import smtplib

from src_0193 import task_func


def test_task_func_default_parameters():
    # Mocking the SMTP class to avoid actual email sending
    class MockSMTP:
        def __init__(self, server, port):
            pass
        
        def starttls(self):
            pass
        
        def login(self, email_address, email_password):
            pass
        
        def sendmail(self, from_addr, to_addrs, msg):
            pass
        
        def quit(self):
            pass
    
    # Using monkeypatch to replace smtplib.SMTP with our mock
    monkeypatch.setattr(smtplib, 'SMTP', MockSMTP)
    
    # Call the function with default parameters
    result = task_func()
    
    # Expected result based on the TEXT constant
    expected_names = [
        "Josie Smith",
        "Mugsy Dog Smith"
    ]
    
    assert result == expected_names

def test_task_func_custom_smtp():
    # Mocking the SMTP class to avoid actual email sending
    class MockSMTP:
        def __init__(self, server, port):
            pass
        
        def starttls(self):
            pass
        
        def login(self, email_address, email_password):
            pass
        
        def sendmail(self, from_addr, to_addrs, msg):
            pass
        
        def quit(self):
            pass
    
    # Using monkeypatch to replace smtplib.SMTP with our mock
    monkeypatch.setattr(smtplib, 'SMTP', MockSMTP)
    
    # Define a custom SMTP function
    def custom_smtp(server, port):
        return MockSMTP(server, port)
    
    # Call the function with a custom SMTP function
    result = task_func(smtp=custom_smtp)
    
    # Expected result based on the TEXT constant
    expected_names = [
        "Josie Smith",
        "Mugsy Dog Smith"
    ]
    
    assert result == expected_names

def test_task_func_empty_text():
    # Mocking the SMTP class to avoid actual email sending
    class MockSMTP:
        def __init__(self, server, port):
            pass
        
        def starttls(self):
            pass
        
        def login(self, email_address, email_password):
            pass
        
        def sendmail(self, from_addr, to_addrs, msg):
            pass
        
        def quit(self):
            pass
    
    # Using monkeypatch to replace smtplib.SMTP with our mock
    monkeypatch.setattr(smtplib, 'SMTP', MockSMTP)
    
    # Call the function with an empty text
    result = task_func(text="")
    
    # Expected result is an empty list
    expected_names = []
    
    assert result == expected_names