python
import os
import binascii
import hashlib
import re
import pytest

from src_0643 import task_func

@pytest.fixture
def directory():
    return './tests/data'

def test_task_func(directory):
    pattern = r"(?<!Distillr)\\AcroTray\.exe"
    hashes = task_func(directory, pattern)
    assert len(hashes) == 1
    assert list(hashes.keys())[0] == os.path.join(directory, 'test.pdf')
    assert hashes[os.path.join(directory, 'test.pdf')] == 'a1a2a3a4a5a6a7a8a9aaabacadaeaf'