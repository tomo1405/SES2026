from src_0643 import task_func


def test_task_func():
    directory = './test_directory'
    pattern = r"(?<!Distillr)\\AcroTray\.exe"
    hashes = task_func(directory, pattern)
    assert hashes == {'path1': 'hash1', 'path2': 'hash2'}