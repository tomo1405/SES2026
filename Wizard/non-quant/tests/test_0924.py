python
import pytest
from src_0924 import task_func

def test_task_func():
    person_names = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams', 'Tom Brown']
    email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    num_records = 3
    
    # Test case 1: Valid input
    expected_df = pd.DataFrame([['John Doe', 'john[at]gmail.com'],
                                ['Jane Smith', 'jane[at]yahoo.com'],
                                ['Bob Johnson', 'bob[at]hotmail.com']],
                               columns=['Name', 'Email'])
    assert task_func(person_names, email_domains, num_records).equals(expected_df)
    
    # Test case 2: Insufficient number of names or domains provided
    with pytest.raises(ValueError):
        task_func([], email_domains, num_records)
        
    with pytest.raises(ValueError):
        task_func(person_names, [], num_records)
        
    with pytest.raises(ValueError):
        task_func(person_names, email_domains, 10)