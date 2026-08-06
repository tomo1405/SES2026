import itertools
import string

import pytest
from src_1031 import task_func


def test_task_func():
    # Call the function to get the DataFrame
    df = task_func()
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (26**3, 3), "DataFrame shape is incorrect"
    
    # Check if the DataFrame has the correct columns
    expected_columns = ["Letter 1", "Letter 2", "Letter 3"]
    assert list(df.columns) == expected_columns, "DataFrame columns are incorrect"
    
    # Check if the DataFrame contains all possible combinations of lowercase letters
    expected_values = list(itertools.product(string.ascii_lowercase, repeat=3))
    assert df.values.tolist() == expected_values, "DataFrame values do not match expected combinations"

# Run the tests
if __name__ == "__main__":
    pytest.main()