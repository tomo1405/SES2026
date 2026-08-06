import pytest
from src_1096 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary directory to store the output file
    with tempfile.TemporaryDirectory() as temp_dir:
        output_filename = os.path.join(temp_dir, 'output.txt')
        
        # Test case 1: Simple text with valid dollar-prefixed words
        text = "This is a $test and another $example."
        expected_output = ["$test", "$example"]
        task_func(text, output_filename)
        
        with open(output_filename, 'r') as file:
            actual_output = file.read().splitlines()
        
        assert actual_output == expected_output

        # Test case 2: Text with only dollar sign
        text = "Just a $ sign."
        expected_output = []
        task_func(text, output_filename)
        
        with open(output_filename, 'r') as file:
            actual_output = file.read().splitlines()
        
        assert actual_output == expected_output

        # Test case 3: Text with dollar-prefixed words followed by punctuation
        text = "Check these: $hello-world and $goodbye!"
        expected_output = ["$hello-world", "$goodbye"]
        task_func(text, output_filename)
        
        with open(output_filename, 'r') as file:
            actual_output = file.read().splitlines()
        
        assert actual_output == expected_output

        # Test case 4: Empty text
        text = ""
        expected_output = []
        task_func(text, output_filename)
        
        with open(output_filename, 'r') as file:
            actual_output = file.read().splitlines()
        
        assert actual_output == expected_output

        # Test case 5: Text with no dollar-prefixed words
        text = "No dollar words here."
        expected_output = []
        task_func(text, output_filename)
        
        with open(output_filename, 'r') as file:
            actual_output = file.read().splitlines()
        
        assert actual_output == expected_output

# Run the tests
if __name__ == "__main__":
    pytest.main()