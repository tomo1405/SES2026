python
import re
import smtplib
import pytest

# Constants
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(text=TEXT, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, recepient_address=RECEPIENT_ADDRESS, smtp=None):

    names = re.findall('(.*?)(?:\\[.*?\\]|$)', text)
    # Remove trailing spaces from each name and filter out empty strings
    names = [name.strip() for name in names if name != ""]
    
    message = 'Subject: Extracted Names\n\n' + '\n'.join(names)
    if smtp:
        server = smtp(smtp_server, smtp_port)
    else:
        server = smtplib.SMTP(smtp_server, smtp_port)
        
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, recepient_address, message)
    server.quit()
    return names

def test_task_func():
    # Test case 1
    assert task_func() == ['Josie Smith', 'Mugsy Dog Smith']
    
    # Test case 2
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]") == ['Josie Smith']
    
    # Test case 3
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]") == ['Josie Smith', 'Mugsy Dog Smith']
    
    # Test case 4
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp_server="smtp.test.com", smtp_port=25) == ['Josie Smith', 'Mugsy Dog Smith']
    
    # Test case 5
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp_server="smtp.test.com", smtp_port=25, email_address="test.email@gmail.com", email_password="test.password", recepient_address="test.names@gmail.com") == ['Josie Smith', 'Mugsy Dog Smith']
    
    # Test case 6
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp=smtplib.SMTP) == ['Josie Smith', 'Mugsy Dog Smith']
    
    # Test case 7
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp=smtplib.SMTP, smtp_server="smtp.test.com", smtp_port=25, email_address="test.email@gmail.com", email_password="test.password", recepient_address="test.names@gmail.com") == ['Josie Smith', 'Mugsy Dog Smith']