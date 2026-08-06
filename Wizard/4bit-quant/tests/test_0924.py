python
import pytest
from src_0924 import task_func

def test_task_func():
    person_names = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams']
    email_domains = ['example.com', 'test.com', 'example.org']
    num_records = 2
    
    with pytest.raises(ValueError):
        task_func([], email_domains)
    
    with pytest.raises(ValueError):
        task_func(person_names, [])
    
    with pytest.raises(ValueError):
        task_func(person_names, email_domains, num_records=10)
    
    df = task_func(person_names, email_domains, num_records=num_records)
    assert df.shape == (num_records, 2)
    assert df.Name.isin(person_names[:num_records]).all()
    assert df.Email.str.contains('@').all()