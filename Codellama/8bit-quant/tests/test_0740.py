import random
import struct

import pytest
from src_0740 import task_func


def test_task_func_with_none():
    assert task_func() in KEYS

def test_task_func_with_hex_key():
    hex_key = random.choice(KEYS)
    assert task_func(hex_key) == round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2)

def test_task_func_with_invalid_hex_key():
    hex_key = '470FC614'
    with pytest.raises(ValueError):
        task_func(hex_key)