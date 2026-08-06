import json
import hashlib
import blake3
import pytest

from src_0341 import task_func

def test_task_func():
    req_data = {"key": "value"}
    blake3_hex, md5_hash = task_func(req_data)
    assert isinstance(blake3_hex, str)
    assert len(blake3_hex) == 64
    assert isinstance(md5_hash, str)
    assert len(md5_hash) == 32