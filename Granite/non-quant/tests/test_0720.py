import re
import os
import glob
import pytest

def task_func(directory, word):
    count = 0
    # Pattern to match word boundaries and ignore case, handling punctuation
    pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
    for filename in glob.glob(os.path.join(directory, '*.*')):
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            if pattern.search(text):
                count += 1
    return count

def test_task_func():
    directory = '/path/to/directory'
    word = 'example'
    expected_count = 5
    actual_count = task_func(directory, word)
    assert actual_count == expected_count, "Expected count does not match actual count"

if __name__ == '__main__':
    pytest.main()