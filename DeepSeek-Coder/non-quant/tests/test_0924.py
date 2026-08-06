import pytest
from src_0924 import task_func

# Test cases for the function

def test_task_func():
    person_names = ["John Doe", "Jane Smith"]
    email_domains = ["example.com", "test.com"]
    num_records = 2

    result = task_func(person_names=person_names, email_domains=email_domains, num_records=num_records)

    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert len(result) == num_records, "The number of records should match the specified number of records"
    assert all(col in result.columns for col in ['Name', 'Email']), "The DataFrame should have the correct columns"

# Add more test cases as needed