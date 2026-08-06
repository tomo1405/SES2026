import codecs
import glob
import os

from src_0726 import task_func


def test_task_func():
    directory = './files/'
    from_encoding = 'cp1251'
    to_encoding = 'utf8'

    task_func(directory, from_encoding, to_encoding)

    for filename in glob.glob(os.path.join(directory, '*.txt')):
        with codecs.open(filename, 'r', from_encoding) as file:
            content = file.read()

        with codecs.open(filename, 'w', to_encoding) as file:
            file.write(content)

    assert os.path.exists(filename)
    assert os.path.isfile(filename)
    assert os.path.getsize(filename) > 0