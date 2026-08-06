import pytest
from src_0564 import task_func

def test_task_func():
    filepath = 'path/to/file.dll'
    destination_dir = 'path/to/destination'

    lib = task_func(filepath, destination_dir)

    assert lib._name == 'file.dll'

    dll_dir = os.path.dirname(filepath)
    dll_files = glob.glob(os.path.join(dll_dir, '*.dll'))

    for dll_file in dll_files:
        assert os.path.exists(os.path.join(destination_dir, dll_file))

    assert os.path.exists(os.path.join(destination_dir, lib._name))