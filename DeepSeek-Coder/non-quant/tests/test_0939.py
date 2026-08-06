import pytest
from src_0939 import task_func
import pandas as pd
import re

# Define test cases
def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'text': ['Hello, World!', 'This is a test.', None, 'Another example.']
    }
    df = pd.DataFrame(data)

    # Call the function with the sample DataFrame
    result = task_func(df)

    # Define the expected results
    expected_results = [
        {'clean_text': 'HelloWorld', 'text_length': 10},
        {'clean_text': 'Thisisatest', 'text_length': 13},
        {'clean_text': '', 'text_length': 0},
        {'clean_text': 'Anotherexample', 'text_length': 13}
    ]

    # Assert the results
    for i, result in enumerate(result):
        assert result[i]['clean_text'] == expected_results[i]['clean_text']
        assert result[i]['text_length'] == expected_results[i]['text_length']

# Run the test
if __name__ == "__main__":
    pytest.main()