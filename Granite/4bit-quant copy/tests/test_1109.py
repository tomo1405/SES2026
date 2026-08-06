import pytest
from collections import Counter
import re

def task_func(result):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    from_user_values = []
    for l_res in result:
        for j in l_res:
            if re.match(regex, j):
                from_user_values.append(l_res[j])
           

    counter = Counter(from_user_values)
    most_common = dict(counter.most_common(1))

    return most_common

def test_task_func():
    result = [
        {'http://www.google.com': 1, 'http://www.facebook.com': 2},
        {'http://www.stackoverflow.com': 3, 'http://www.yahoo.com': 4},
        {'http://www.amazon.com': 5, 'http://www.wikipedia.com': 6}
    ]
    expected_output = {'http://www.google.com': 1}
    actual_output = task_func(result)
    assert actual_output == expected_output

if __name__ == "__main__":
    pytest.main()