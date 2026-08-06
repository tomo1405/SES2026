from glob import glob
from unittest.mock import patch

import pytest
from src_0401 import task_func


@pytest.mark.parametrize(
    "directory, string, expected_output",
    [
        (
            "/path/to/directory",
            "example_string",
            ["path/to/directory/file1.json", "path/to/directory/subdirectory/file2.json"],
        ),
        (
            "/another/path/to/directory",
            "another_example_string",
            ["another/path/to/directory/file3.json"],
        ),
    ],
)
def test_task_func(directory, string, expected_output):
    json_files = glob(f"{directory}/**/*.json", recursive=True)

    with patch("pathlib.Path.rglob", return_value=json_files):
        assert task_func(directory, string) == expected_output