import glob

from pytest import mark


@mark.parametrize("directory_path, expected_output", [
    ("/path/to/directory", 5),
    ("/another/path/to/directory", 10),
    ("/some/other/path/to/directory", 0),
])
def test_task_func(directory_path, expected_output):
    docx_files = glob.glob(directory_path + '/*.docx')
    processed_files = task_func(directory_path)
    assert processed_files == expected_output