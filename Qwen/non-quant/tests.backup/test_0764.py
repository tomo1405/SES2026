import pytest
from src_0764 import task_func
import numpy as np
import json
import csv
from io import StringIO

@pytest.fixture
def input_data():
    return '[{"a": 1, "b": 2}, {"a": 3, "b": 4}]'

@pytest.fixture
def expected_output():
    return {
        'a': {'mean': 2.0, 'median': 2.0},
        'b': {'mean': 3.0, 'median': 3.0}
    }

def test_task_func(tmpdir, input_data, expected_output):
    # Create a temporary input file
    input_file = tmpdir.join('input.json')
    input_file.write(input_data)

    # Create a temporary output file
    output_file = tmpdir.join('output.csv')

    # Call the function
    result = task_func(str(input_file), str(output_file))

    # Check if the result matches the expected output
    assert result == expected_output

    # Read the output CSV file and check its contents
    with open(output_file, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 2
        assert rows[0] == {'key': 'a', 'mean': '2.0', 'median': '2.0'}
        assert rows[1] == {'key': 'b', 'mean': '3.0', 'median': '3.0'}