import pytest
from src_0632 import task_func

def test_task_func():
    # Test that the function returns the correct file path
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    filename = 'test_file.csv'
    output_dir = './output'
    expected_file_path = os.path.join(output_dir, filename)
    assert task_func(df, filename, output_dir) == expected_file_path

    # Test that the function creates the output directory if it doesn't exist
    output_dir = './output_new'
    expected_file_path = os.path.join(output_dir, filename)
    assert task_func(df, filename, output_dir) == expected_file_path
    assert os.path.exists(output_dir)

    # Test that the function writes the correct data to the file
    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    filename = 'test_file.csv'
    output_dir = './output'
    expected_file_path = os.path.join(output_dir, filename)
    task_func(df, filename, output_dir)
    with open(expected_file_path, 'r') as f:
        assert f.read() == 'a,b\n1,4\n2,5\n3,6\n'