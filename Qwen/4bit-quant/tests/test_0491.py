import json
import os

from src_0491 import task_func


def test_task_func():
    # Test XML string
    xml_string = """
    <root>
        <child>Value</child>
    </root>
    """
    
    # Temporary file path
    temp_file_path = "temp_test_file.json"
    
    try:
        # Call the function
        result = task_func(xml_string, temp_file_path)
        
        # Check if the result is a dictionary
        assert isinstance(result, dict), "The result should be a dictionary."
        
        # Check if the dictionary matches the expected structure
        expected_dict = {
            'root': {
                'child': 'Value'
            }
        }
        assert result == expected_dict, f"Result does not match the expected dictionary. Got {result}, expected {expected_dict}"
        
        # Check if the file was created and contains the correct data
        assert os.path.exists(temp_file_path), "The JSON file was not created."
        
        with open(temp_file_path, 'r') as json_file:
            file_content = json.load(json_file)
            assert file_content == expected_dict, "The content of the JSON file does not match the expected dictionary."
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)