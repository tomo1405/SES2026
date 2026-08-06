import pytest
from src_0491 import task_func
import os
import xmltodict
import json

def test_task_func(tmpdir):
    # Create a sample XML string
    xml_string = """
    <root>
        <child>Value</child>
    </root>
    """
    
    # Define the expected dictionary
    expected_dict = {
        'root': {
            'child': 'Value'
        }
    }
    
    # Create a temporary file path
    temp_file = tmpdir.join("output.json")
    
    # Call the function
    result_dict = task_func(xml_string, str(temp_file))
    
    # Check if the returned dictionary matches the expected dictionary
    assert result_dict == expected_dict
    
    # Check if the JSON file was created and contains the correct data
    with open(str(temp_file), 'r') as json_file:
        saved_dict = json.load(json_file)
    
    assert saved_dict == expected_dict