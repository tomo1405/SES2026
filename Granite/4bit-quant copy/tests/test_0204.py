import pytest
from src_0204 import task_func

def test_task_func():
    input_data = '{"recipient": "recipient@example.com", "names": ["Alice", "Bob", "Charlie"]}'
    expected_output = ['Alice', 'Bob', 'Charlie']
    
    # Test with smtp server
    output = task_func(input_data=input_data)
    assert output == expected_output
    
    # Test with smtp server object
    from src_0204 import SMTP_SERVER, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD
    from smtplib import SMTP
    smtp = SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    output = task_func(input_data=input_data, smtp=smtp)
    assert output == expected_output