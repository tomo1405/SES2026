from src_0643 import task_func


def test_task_func():
    directory = './output'
    pattern = r"(?<!Distillr)\\AcroTray\.exe"
    hashes = task_func(directory, pattern)
    assert isinstance(hashes, dict)
    for path, hash_value in hashes.items():
        assert isinstance(path, str)
        assert isinstance(hash_value, str)
        assert len(hash_value) == 64