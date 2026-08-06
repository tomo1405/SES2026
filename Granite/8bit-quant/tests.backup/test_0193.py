import pytest
from src_0193 import task_func

def test_task_func():
    assert task_func() == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_text():
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]") == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_recepient_address():
    assert task_func(recepient_address="names@gmail.com") == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_smtp_server():
    assert task_func(smtp_server="smtp.gmail.com") == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_smtp_port():
    assert task_func(smtp_port=587) == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_email_address():
    assert task_func(email_address="your.email@gmail.com") == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_email_password():
    assert task_func(email_password="your.password") == ["Josie Smith", "Mugsy Dog Smith"]

def test_task_func_with_all_parameters():
    assert task_func(text="Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]", smtp_server="smtp.gmail.com", smtp_port=587, email_address="your.email@gmail.com", email_password="your.password", recepient_address="names@gmail.com") == ["Josie Smith", "Mugsy Dog Smith"]