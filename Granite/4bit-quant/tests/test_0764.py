import json

from src_0764 import task_func


def test_task_func():
    input_file = 'input.json'
    output_file = 'output.csv'
    
    # Mock the input file and expected output file
    with open(input_file, 'w') as f:
        json.dump([{'key1': 1, 'key2': 2}, {'key1': 3, 'key2': 4}], f)
    
    expected_output = {'key1': {'mean': 2.0, 'median': 2.0}, 'key2': {'mean': 3.0, 'median': 3.0}}
    
    # Call the function and assert the output against the expected output
    result = task_func(input_file, output_file)
    assert result == expected_output