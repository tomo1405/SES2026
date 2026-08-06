python
import pytest
from src_0776 import task_func

def test_task_func():
    # Test case 1
    assert task_func("abc-def") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
    # Test case 2
    assert task_func("abc-def-ghi") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1}
    # Test case 3
    assert task_func("abc-") == {'a': 1, 'b': 1, 'c': 1}
    # Test case 4
    assert task_func("abc") == {}
    # Test case 5
    assert task_func("a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    # Test case 6
    assert task_func("123-456") == {}
    # Test case 7
    assert task_func("aBc-dEf-gHi-jKl-mNo-pQr-sTu-vWx-yYz") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    # Test case 8
    assert task_func("aBc-dEf-gHi-jKl-mNo-pQr-sTu-vWx-yYz-123") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    # Test case 9
    assert task_func("aBc-dEf-gHi-jKl-mNo-pQr-sTu-vWx-yYz-123-456") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    # Test case 10
    assert task_func("aBc-dEf-gHi-jKl-mNo-pQr-sTu-vWx-yYz-123-456-789") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}