python
import pytest
from src_1096 import task_func

def test_task_func():
    text = "This is a sample text with $100 and $200 dollars."
    output_filename = "output.txt"

    expected_output = os.path.abspath(output_filename)

    # Test case 1: Valid input
    assert task_func(text, output_filename) == expected_output

    # Test case 2: Invalid input (empty text)
    with pytest.raises(ValueError):
        task_func("", output_filename)

    # Test case 3: Invalid input (empty output filename)
    with pytest.raises(ValueError):
        task_func(text, "")

    # Test case 4: Invalid input (output filename with invalid characters)
    with pytest.raises(ValueError):
        task_func(text, "output.txtx")

    # Test case 5: Invalid input (output filename with invalid path)
    with pytest.raises(ValueError):
        task_func(text, "/invalid/path/output.txt")