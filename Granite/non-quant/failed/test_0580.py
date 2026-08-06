import pytest
from src_0580 import task_func

def test_task_func():
    csv_file = 'test_file.csv'
    with open(csv_file, 'w') as file:
        file.write('word1,word2,word3\n')
        file.write('Word1,Word2,Word3\n')
        file.write('WORD1,WORD2,WORD3\n')
    ax, most_common_words = task_func(csv_file)
    assert ax is not None
    assert most_common_words == [('word1', 3), ('word2', 3), ('word3', 3)]

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent_file.csv')

def test_task_func_io_error():
    with open('test_file.csv', 'w') as file:
        file.write('word1,word2,word3')
    with pytest.raises(IOError):
        task_func('test_file.csv')