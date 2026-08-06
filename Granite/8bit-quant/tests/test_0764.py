import pytest
from src_0764 import task_func

def test_task_func():
    input_file = 'input.json'
    output_file = 'output.csv'
    
    result = task_func(input_file, output_file)
    
    assert result is not None
    assert isinstance(result, dict)
    
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            assert 'key' in row
            assert 'mean' in row
            assert 'median' in row