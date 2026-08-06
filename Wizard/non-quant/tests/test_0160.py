python
import struct
import io
import gzip
import pytest

def task_func(newArray):
    buffer = io.BytesIO()

    with gzip.GzipFile(fileobj=buffer, mode='w') as f:
        f.write(struct.pack('d'*newArray.size, *newArray))

    return buffer.getvalue()

def test_task_func():
    newArray = numpy.array([1.0, 2.0, 3.0])
    result = task_func(newArray)
    assert result == b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xca\xccMU(\xc9,I-.\x04\x00\xf3\xf3\x01\x00\x00\x00'