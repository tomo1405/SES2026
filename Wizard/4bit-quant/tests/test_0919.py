python
import pandas as pd
import re
import pytest

# Test data
data = {'name': ['John', 'Jane', 'Bob'], 'age': [25, 30, 40], 'address': ['123 Main St', '456 Oak Ave', '789 Elm St']}
mapping = {'JAN': 'January', 'BOB': 'Bob', 'ST': 'Street'}

# Test function
def test_task_func():
    df = pd.DataFrame(data)
    pattern = re.compile(r'\b[A-Z]+\b')
    
    def replace_match(match):
        return mapping.get(match.group(0), match.group(0))

    df = df.applymap(lambda x: pattern.sub(replace_match, x) if isinstance(x, str) else x)

    assert df.equals(pd.DataFrame({'name': ['John', 'Jane', 'Bob'], 'age': [25, 30, 40], 'address': ['123 Main St', '456 Oak Ave', '789 Elm St']}))