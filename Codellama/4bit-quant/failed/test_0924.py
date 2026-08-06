import pytest
from src_0924 import task_func

def test_task_func():
    person_names = ['John Doe', 'Jane Doe', 'Jim Bob']
    email_domains = ['example.com', 'example.org']
    num_records = 5

    df = task_func(person_names, email_domains, num_records)

    assert len(df) == num_records
    assert 'Name' in df.columns
    assert 'Email' in df.columns

    for i in range(num_records):
        name = df.iloc[i]['Name']
        email = df.iloc[i]['Email']
        assert re.match(r'^[a-zA-Z]+ [a-zA-Z]+$', name)
        assert re.match(r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$', email)

    assert df.iloc[0]['Name'] == 'John Doe'
    assert df.iloc[0]['Email'] == 'john.doe[at]example.com'
    assert df.iloc[1]['Name'] == 'Jane Doe'
    assert df.iloc[1]['Email'] == 'jane.doe[at]example.org'
    assert df.iloc[2]['Name'] == 'Jim Bob'
    assert df.iloc[2]['Email'] == 'jim.bob[at]example.com'