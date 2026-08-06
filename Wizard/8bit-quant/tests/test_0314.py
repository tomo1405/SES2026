python
import pytest
from src_0314 import task_func

def test_task_func():
    directory = 'test_directory'
    os.makedirs(directory)
    with open(os.path.join(directory, 'file1.txt'), 'w') as file:
        file.write('content1[subdirectory1]')
    with open(os.path.join(directory, 'file2.txt'), 'w') as file:
        file.write('content2[subdirectory2]')
    with open(os.path.join(directory, 'file3.txt'), 'w') as file:
        file.write('content3[subdirectory1]')
    with open(os.path.join(directory, 'file4.txt'), 'w') as file:
        file.write('content4[subdirectory2]')

    result = task_func(directory)

    assert result[0] == directory
    assert result[1]['subdirectory1'] == ['file1_20220314123456.txt', 'file3_20220314123456.txt']
    assert result[1]['subdirectory2'] == ['file2_20220314123456.txt', 'file4_20220314123456.txt']

    shutil.rmtree(directory)