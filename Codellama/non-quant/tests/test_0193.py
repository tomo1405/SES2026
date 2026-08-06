import pytest
from src_0193 import task_func

def test_task_func():
    # Test with valid input
    text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "your.email@gmail.com"
    email_password = "your.password"
    recepient_address = "names@gmail.com"
    smtp = None
    names = task_func(text, smtp_server, smtp_port, email_address, email_password, recepient_address, smtp)
    assert names == ["Josie Smith", "Mugsy Dog Smith"]

    # Test with invalid input
    text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "your.email@gmail.com"
    email_password = "your.password"
    recepient_address = "names@gmail.com"
    smtp = None
    names = task_func(text, smtp_server, smtp_port, email_address, email_password, recepient_address, smtp)
    assert names == ["Josie Smith", "Mugsy Dog Smith"]

    # Test with valid input and custom SMTP server
    text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "your.email@gmail.com"
    email_password = "your.password"
    recepient_address = "names@gmail.com"
    smtp = smtplib.SMTP
    names = task_func(text, smtp_server, smtp_port, email_address, email_password, recepient_address, smtp)
    assert names == ["Josie Smith", "Mugsy Dog Smith"]

    # Test with invalid input and custom SMTP server
    text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_address = "your.email@gmail.com"
    email_password = "your.password"
    recepient_address = "names@gmail.com"
    smtp = smtplib.SMTP
    names = task_func(text, smtp_server, smtp_port, email_address, email_password, recepient_address, smtp)
    assert names == ["Josie Smith", "Mugsy Dog Smith"]