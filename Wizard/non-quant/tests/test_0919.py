python
import pandas as pd
import re
import pytest

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    df = pd.DataFrame(data)
    pattern = re.compile(r'\b[A-Z]+\b')
    
    def replace_match(match):
        return mapping.get(match.group(0), match.group(0))

    df = df.applymap(lambda x: pattern.sub(replace_match, x) if isinstance(x, str) else x)

    return df

# Test case 1
def test_task_func_1():
    data = {'col1': ['ABC', 'DEF', 'GHI'], 'col2': ['JKL', 'MNO', 'PQR']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Beta', 'GHI': 'Gamma'}
    expected_result = {'col1': ['Alpha', 'Beta', 'Gamma'], 'col2': ['JKL', 'MNO', 'PQR']}
    result = task_func(data, mapping)
    assert result.equals(pd.DataFrame(expected_result))

# Test case 2
def test_task_func_2():
    data = {'col1': ['ABC', 'DEF', 'GHI'], 'col2': ['JKL', 'MNO', 'PQR']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Beta', 'GHI': 'Gamma', 'XYZ': 'Zeta'}
    expected_result = {'col1': ['Alpha', 'Beta', 'Gamma'], 'col2': ['JKL', 'MNO', 'PQR']}
    result = task_func(data, mapping)
    assert result.equals(pd.DataFrame(expected_result))

# Test case 3
def test_task_func_3():
    data = {'col1': ['ABC', 'DEF', 'GHI'], 'col2': ['JKL', 'MNO', 'PQR']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Beta', 'GHI': 'Gamma', 'XYZ': 'Zeta', '123': 'One Two Three'}
    expected_result = {'col1': ['Alpha', 'Beta', 'Gamma'], 'col2': ['JKL', 'MNO', 'PQR']}
    result = task_func(data, mapping)
    assert result.equals(pd.DataFrame(expected_result))

# Test case 4
def test_task_func_4():
    data = {'col1': ['ABC', 'DEF', 'GHI'], 'col2': ['JKL', 'MNO', 'PQR']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Beta', 'GHI': 'Gamma', 'XYZ': 'Zeta', '123': 'One Two Three', 'JKL': 'John'}
    expected_result = {'col1': ['Alpha', 'Beta', 'Gamma'], 'col2': ['John', 'MNO', 'PQR']}
    result = task_func(data, mapping)
    assert result.equals(pd.DataFrame(expected_result))

# Test case 5
def test_task_func_5():
    data = {'col1': ['ABC', 'DEF', 'GHI'], 'col2': ['JKL', 'MNO', 'PQR']}
    mapping = {'ABC': 'Alpha', 'DEF': 'Beta', 'GHI': 'Gamma', 'XYZ': 'Zeta', '123': 'One Two Three', 'JKL': 'John', 'MNO': 'Mike'}
    expected_result = {'col1': ['Alpha', 'Beta', 'Gamma'], 'col2': ['John', 'Mike', 'PQR']}
    result = task_func(data, mapping)
    assert result.equals(pd.DataFrame(expected_result))