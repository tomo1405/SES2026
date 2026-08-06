import pytest
from src_0054 import task_func
import pandas as pd
import io

def test_task_func():
    # Mock input text
    input_text = """Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA
Name: Jane Smith, Email: jane.smith@example.com, Age: 25, Country: Canada"""

    # Expected DataFrame
    expected_data = {
        "Name": ["John Doe", "Jane Smith"],
        "Email": ["john.doe@example.com", "jane.smith@example.com"],
        "Age": [30, 25],
        "Country": ["USA", "Canada"]
    }
    expected_df = pd.DataFrame(expected_data)

    # Redirect stdout to capture the plot
    captured_output = io.StringIO()
    import sys
    sys.stdout = captured_output

    # Call the function
    result_df = task_func(input_text)

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check if the returned DataFrame is correct
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check if the plot was generated (basic check, not a deep one)
    assert "histplot" in captured_output.getvalue(), "The plot was not generated"