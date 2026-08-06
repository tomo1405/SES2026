import pytest
from src_0712 import task_func

def test_task_func():
    json_file = 'test.json'
    csv_file = 'test.csv'
    
    # Mock the input and expected output files
    with open(json_file, 'w') as f:
        f.write('{"name": "John", "age": 30}')
    
    expected_csv_file = 'expected.csv'
    with open(expected_csv_file, 'w') as f:
        f.write('name,age\nJohn,30\n')
    
    # Call the function and assert the output file matches the expected one
    output_csv_file = task_func(json_file, csv_file)
    with open(output_csv_file, 'r') as f:
        output_data = f.read()
    
    with open(expected_csv_file, 'r') as f:
        expected_data = f.read()
    
    assert output_data == expected_data