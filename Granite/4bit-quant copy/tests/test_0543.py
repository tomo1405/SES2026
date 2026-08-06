import hashlib
import random
import struct
from src_0543 import task_func

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def test_task_func():
    random.seed(42)
    hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    hashed_float = hashlib.md5(str(float_num).encode()).hexdigest()
    assert task_func(hex_keys=KEYS, seed=42) == hashed_float

def test_task_func_invalid_hex_key():
    with pytest.raises(ValueError) as e:
        task_func(hex_keys=['invalid_key'], seed=42)
    assert "Invalid hexadecimal string in hex_keys." in str(e.value)