import pytest
from collections import Counter
import itertools
import string
from src_0929 import task_func

def test_task_func():
    word = "example"
    result = task_func(word)
    expected_result = {
        'aa': 0, 'ab': 0, 'ac': 0, 'ad': 0, 'ae': 0, 'ba': 0, 'bb': 1, 'bc': 0, 'bd': 0, 'be': 0,
        'ca': 0, 'cb': 0, 'cc': 0, 'cd': 0, 'ce': 0, 'da': 0, 'db': 0, 'dc': 0, 'dd': 0, 'de': 0,
        'ea': 0, 'eb': 0, 'ec': 0, 'ed': 0, 'ee': 0,
        'aaa': 0, 'aab': 0, 'aac': 0, 'aad': 0, 'aae': 0, 'aba': 0, 'abb': 0, 'abc': 0, 'abd': 0, 'abe': 0,
        'aca': 0, 'acb': 0, 'acc': 0, 'acd': 0, 'ace': 0, 'ada': 0, 'adb': 0, 'adc': 0, 'add': 0, 'ade': 0,
        'aea': 0, 'aeb': 0, 'aec': 0, 'aed': 0, 'aee': 0,
        'aaaa': 0, 'aaab': 0, 'aaac': 0, 'aaad': 0, 'aaae': 0, 'abaa': 0, 'abab': 0, 'abac': 0, 'abad': 0, 'abae': 0,
        'acaa': 0, 'acab': 0, 'acac': 0, 'acad': 0, 'acae': 0, 'adaa': 0, 'adab': 0, 'adac': 0, 'adad': 0, 'adae': 0,
        'aeaa': 0, 'aeab': 0, 'aeac': 0, 'aead': 0, 'aeae': 0,
    }
    assert result == expected_result

def test_task_func_with_empty_string():
    word = ""
    result = task_func(word)
    expected_result = {
        'aa': 0, 'ab': 0, 'ac': 0, 'ad': 0, 'ae': 0, 'ba': 0, 'bb': 0, 'bc': 0, 'bd': 0, 'be': 0,
        'ca': 0, 'cb': 0, 'cc': 0, 'cd': 0, 'ce': 0, 'da': 0, 'db': 0, 'dc': 0, 'dd': 0, 'de': 0,
        'ea': 0, 'eb': 0, 'ec': 0, 'ed': 0, 'ee': 0,
        'aaa': 0, 'aab': 0, 'aac': 0, 'aad': 0, 'aae': 0, 'aba': 0, 'abb': 0, 'abc': 0, 'abd': 0, 'abe': 0,
        'aca': 0, 'acb': 0, 'acc': 0, 'acd': 0, 'ace': 0, 'ada': 0, 'adb': 0, 'adc': 0, 'add': 0, 'ade': 0,
        'aea': 0, 'aeb': 0, 'aec': 0, 'aed': 0, 'aee': 0,
        'aaaa': 0, 'aaab': 0, 'aaac': 0, 'aaad': 0, 'aaae': 0, 'abaa': 0, 'abab': 0, 'abac': 0, 'abad': 0, 'abae': 0,
        'acaa': 0, 'acab': 0, 'acac': 0, 'acad': 0, 'acae': 0, 'adaa': 0, 'adab': 0, 'adac': 0, 'adad': 0, 'adae': 0,
        'aeaa': 0, 'aeab': 0, 'aeac': 0, 'aead': 0, 'aeae': 0,
    }
    assert result == expected_result

def test_task_func_with_single_letter():
    word = "a"
    result = task_func(word)
    expected_result = {
        'aa': 0, 'ab': 0, 'ac': 0, 'ad': 0, 'ae': 0, 'ba': 0, 'bb': 0, 'bc': 0, 'bd': 0, 'be': 0,
        'ca': 0, 'cb': 0, 'cc': 0, 'cd': 0, 'ce': 0, 'da': 0, 'db': 0, 'dc': 0, 'dd': 0, 'de': 0,
        'ea': 0, 'eb': 0, 'ec': 0, 'ed': 0, 'ee': 0,
        'aaa': 0, 'aab': 0, 'aac': 0, 'aad': 0, 'aae': 0, 'aba': 0, 'abb': 0, 'abc': 0, 'abd': 0, 'abe': 0,
        'aca': 0, 'acb': 0, 'acc': 0, 'acd': 0, 'ace': 0, 'ada': 0, 'adb': 0, 'adc': 0, 'add': 0, 'ade': 0,
        'aea': 0, 'aeb': 0, 'aec': 0, 'aed': 0, 'aee': 0,
        'aaaa': 0, 'aaab': 0, 'aaac': 0, 'aaad': 0, 'aaae': 0, 'abaa': 0, 'abab': 0, 'abac': 0, 'abad': 0, 'abae': 0,
        'acaa': 0, 'acab': 0, 'acac': 0, 'acad': 0, 'acae': 0, 'adaa': 0, 'adab': 0, 'adac': 0, 'adad': 0, 'adae': 0,
        'aeaa': 0, 'aeab': 0, 'aeac': 0, 'aead': 0, 'aeae': 0,
    }
    assert result == expected_result