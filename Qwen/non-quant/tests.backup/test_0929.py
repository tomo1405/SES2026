import pytest
from src_0929 import task_func

def test_task_func_empty_string():
    result = task_func("")
    assert result == {}

def test_task_func_single_character():
    result = task_func("a")
    assert result == {}

def test_task_func_two_characters():
    result = task_func("ab")
    expected = {'ab': 1, 'ba': 0, 'aa': 0, 'bb': 0, 'cc': 0, 'dd': 0, 'ee': 0, 'ff': 0, 'gg': 0, 'hh': 0, 'ii': 0, 'jj': 0, 'kk': 0, 'll': 0, 'mm': 0, 'nn': 0, 'oo': 0, 'pp': 0, 'qq': 0, 'rr': 0, 'ss': 0, 'tt': 0, 'uu': 0, 'vv': 0, 'ww': 0, 'xx': 0, 'yy': 0, 'zz': 0}
    assert result == expected

def test_task_func_multiple_characters():
    result = task_func("banana")
    expected = {'ba': 1, 'an': 2, 'na': 1, 'ab': 0, 'bc': 0, 'cd': 0, 'de': 0, 'ef': 0, 'fg': 0, 'gh': 0, 'hi': 0, 'ij': 0, 'jk': 0, 'kl': 0, 'lm': 0, 'mn': 0, 'no': 0, 'op': 0, 'pq': 0, 'qr': 0, 'rs': 0, 'st': 0, 'tu': 0, 'uv': 0, 'vw': 0, 'wx': 0, 'xy': 0, 'yz': 0, 'aa': 0, 'bb': 0, 'cc': 0, 'dd': 0, 'ee': 0, 'ff': 0, 'gg': 0, 'hh': 0, 'ii': 0, 'jj': 0, 'kk': 0, 'll': 0, 'mm': 0, 'nn': 0, 'oo': 0, 'pp': 0, 'qq': 0, 'rr': 0, 'ss': 0, 'tt': 0, 'uu': 0, 'vv': 0, 'ww': 0, 'xx': 0, 'yy': 0, 'zz': 0}
    assert result == expected

def test_task_func_all_unique_characters():
    result = task_func("abcdef")
    expected = {'ab': 1, 'bc': 1, 'cd': 1, 'de': 1, 'ef': 1, 'fa': 0, 'ac': 0, 'ad': 0, 'ae': 0, 'af': 0, 'bd': 0, 'be': 0, 'bf': 0, 'ce': 0, 'cf': 0, 'df': 0, 'aa': 0, 'bb': 0, 'cc': 0, 'dd': 0, 'ee': 0, 'ff': 0, 'gg': 0, 'hh': 0, 'ii': 0, 'jj': 0, 'kk': 0, 'll': 0, 'mm': 0, 'nn': 0, 'oo': 0, 'pp': 0, 'qq': 0, 'rr': 0, 'ss': 0, 'tt': 0, 'uu': 0, 'vv': 0, 'ww': 0, 'xx': 0, 'yy': 0, 'zz': 0}
    assert result == expected

def test_task_func_repeated_characters():
    result = task_func("aabbcc")
    expected = {'ab': 2, 'bc': 2, 'ca': 0, 'ba': 0, 'cb': 0, 'ac': 0, 'ad': 0, 'ae': 0, 'af': 0, 'ag': 0, 'ah': 0, 'ai': 0, 'aj': 0, 'ak': 0, 'al': 0, 'am': 0, 'an': 0, 'ao': 0, 'ap': 0, 'aq': 0, 'ar': 0, 'as': 0, 'at': 0, 'au': 0, 'av': 0, 'aw': 0, 'ax': 0, 'ay': 0, 'az': 0, 'aa': 3, 'bb': 3, 'cc': 3, 'dd': 0, 'ee': 0, 'ff': 0, 'gg': 0, 'hh': 0, 'ii': 0, 'jj': 0, 'kk': 0, 'll': 0, 'mm': 0, 'nn': 0, 'oo': 0, 'pp': 0, 'qq': 0, 'rr': 0, 'ss': 0, 'tt': 0, 'uu': 0, 'vv': 0, 'ww': 0, 'xx': 0, 'yy': 0, 'zz': 0}
    assert result == expected