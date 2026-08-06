import pytest
from src_0193 import task_func

def test_task_func():
    # Test with default arguments
    names = task_func()
    assert names == ['Josie Smith', 'Mugsy Dog Smith']

    # Test with custom arguments
    names = task_func(text='Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]',
                      smtp_server='smtp.gmail.com',
                      smtp_port=587,
                      email_address='your.email@gmail.com',
                      email_password='your.password',
                      recepient_address='names@gmail.com')
    assert names == ['Josie Smith', 'Mugsy Dog Smith']

    # Test with custom smtp server
    names = task_func(text='Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]',
                      smtp_server='smtp.example.com',
                      smtp_port=587,
                      email_address='your.email@gmail.com',
                      email_password='your.password',
                      recepient_address='names@gmail.com')
    assert names == ['Josie Smith', 'Mugsy Dog Smith']

    # Test with custom email address
    names = task_func(text='Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]',
                      smtp_server='smtp.gmail.com',
                      smtp_port=587,
                      email_address='your.email@example.com',
                      email_password='your.password',
                      recepient_address='names@gmail.com')
    assert names == ['Josie Smith', 'Mugsy Dog Smith']

    # Test with custom email password
    names = task_func(text='Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]',
                      smtp_server='smtp.gmail.com',
                      smtp_port=587,
                      email_address='your.email@gmail.com',
                      email_password='your.password',
                      recepient_address='names@gmail.com')
    assert names == ['Josie Smith', 'Mugsy Dog Smith']

    # Test with custom recepient address
    names = task_func(text='Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]',
                      smtp_server='smtp.gmail.com',
                      smtp_port=587,
                      email_address='your.email@gmail.com',
                      email_password='your.password',
                      recepient_address='names@example.com')
    assert names == ['Josie Smith', 'Mugsy Dog Smith']