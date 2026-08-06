import pytest
from src_0491 import task_func
import os
import xmltodict
import json

def test_task_func():
    # Sample XML string
    xml_string = """
    <root>
        <child>Value</child>
    </root>
    """
    
    # Define a temporary file path
    temp_file_path = "temp_test.json"
    
    # Call the function
    result = task_func(xml_string, temp_file_path)
    
    # Expected dictionary
    expected_dict = {
        'root': {
            'child': 'Value'
        }
    }
    
    # Check if the returned dictionary is correct
    assert result == expected_dict
    
    # Check if the JSON file was created and contains the correct data
    with open(temp_file_path, 'r') as json_file:
        content = json.load(json_file)
        assert content == expected_dict
    
    # Clean up the temporary file
    os.remove(temp_file_path)