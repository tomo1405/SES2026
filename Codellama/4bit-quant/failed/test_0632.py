import pytest
from src_0632 import task_func

def test_task_func():
    # Test that the function returns the correct file path
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    filename = 'test.csv'
    output_dir = './output'
    expected_file_path = os.path.join(output_dir, filename)
    assert task_func(df, filename, output_dir) == expected_file_path

    # Test that the function creates the output directory if it doesn't exist
    output_dir = './output2'
    expected_file_path = os.path.join(output_dir, filename)
    assert task_func(df, filename, output_dir) == expected_file_path

    # Test that the function raises an error if the output directory is not a string
    with pytest.raises(TypeError):
        task_func(df, filename, 123)

    # Test that the function raises an error if the output directory is not a valid path
    with pytest.raises(ValueError):
        task_func(df, filename, 'invalid/path')