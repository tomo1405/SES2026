python
import pytest
from src_0764 import task_func

def test_task_func():
    input_file = 'input.json'
    output_file = 'output.csv'
    expected_result = {'a': {'mean': 1.0, 'median': 1.0}, 'b': {'mean': 2.0, 'median': 2.0}, 'c': {'mean': 3.0, 'median': 3.0}}
    
    with open(input_file, 'w') as f:
        json.dump([{'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'c': 3}], f)
    
    task_func(input_file, output_file)
    
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        result = {row['key']: {'mean': float(row['mean']), 'median': float(row['median'])} for row in reader}
    
    assert result == expected_result
    
    # Clean up
    import os
    os.remove(input_file)
    os.remove(output_file)