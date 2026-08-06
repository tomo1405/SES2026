python
import pytest
from src_0924 import task_func

def test_task_func():
    person_names = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams']
    email_domains = ['example.com', 'example.org']
    num_records = 2
    
    with pytest.raises(ValueError):
        task_func(person_names, email_domains, num_records)
        
    person_names = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams']
    email_domains = ['example.com', 'example.org']
    num_records = 4
    
    df = task_func(person_names, email_domains, num_records)
    assert df.shape == (4, 2)
    assert df.iloc[0, 0] == 'Jane Smith'
    assert df.iloc[0, 1] == 'jane[at]example.com'
    assert df.iloc[1, 0] == 'Bob Johnson'
    assert df.iloc[1, 1] == 'bob[at]example.com'
    assert df.iloc[2, 0] == 'Alice Williams'
    assert df.iloc[2, 1] == 'alice[at]example.com'
    assert df.iloc[3, 0] == 'John Doe'
    assert df.iloc[3, 1] == 'john[at]example.com'