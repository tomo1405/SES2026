import pytest
from src_0630 import task_func


def test_task_func_output_dir_exists():
    dataset = [pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
               pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    assert os.path.exists(output_dir)


def test_task_func_output_file_exists():
    dataset = [pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
               pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    filepath = os.path.join(output_dir, filename)
    assert os.path.exists(filepath)


def test_task_func_output_file_content():
    dataset = [pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
               pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        assert content == 'a,b\n1,4\n2,5\n3,6\n------\n7,10\n8,11\n9,12\n'


def test_task_func_output_file_separator():
    dataset = [pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
               pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        assert content.count('------\n') == 1


def test_task_func_output_file_newline():
    dataset = [pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
               pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()
        assert content.count('\n') == 4