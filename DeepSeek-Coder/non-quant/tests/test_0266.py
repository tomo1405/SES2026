import pytest
from src_0266 import task_func

def test_task_func():
    # Test data
    data = {'a': 1, 'b': 2, 'c': 3}
    
    # Call the function
    result = task_func(data)
    
    # Check the output
    assert os.path.exists(result), "The JSON file was not created."
    
    # Read the JSON file and check the content
    with open(result, 'r') as file:
        json_data = json.load(file)
        assert json_data['data'] == data
        assert json_data['freq'] == collections.Counter(data.values())

    # Clean up by removing the JSON file
    os.remove(result)