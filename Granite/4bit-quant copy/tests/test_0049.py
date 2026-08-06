import pytest
from src_0049 import task_func

def test_task_func():
    n = 100  # Number of timestamps to generate
    output_path = "output.png"  # Path to save the histogram plot

    timestamps = task_func(n, output_path)

    assert len(timestamps) == n  # Check if the number of timestamps is correct
    assert isinstance(timestamps[0], str)  # Check if the timestamps are strings
    assert any(output_path in timestamp for timestamp in timestamps)  # Check if the output path is included in the timestamps

    # You can add more assertions based on your specific requirements

if __name__ == "__main__":
    pytest.main()