import pytest
from src_1096 import task_func

def test_task_func():
    text = "This is a sample text with $100 and $200 in it."
    output_filename = "output.txt"
    expected_output_path = "/path/to/expected/output.txt"

    result = task_func(text, output_filename)

    assert result == expected_output_path
    assert os.path.exists(output_filename)
    with open(output_filename, 'r') as file:
        lines = file.readlines()
        assert lines == ["$100\n", "$200\n"]

if __name__ == "__main__":
    pytest.main()