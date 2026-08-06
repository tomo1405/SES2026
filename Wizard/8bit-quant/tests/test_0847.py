python
import collections
import pandas as pd
import pytest

def task_func(obj_list, attr):
    attr_values = [getattr(obj, attr) for obj in obj_list]
    count = collections.Counter(attr_values)
    if len(count.keys()) == 0:
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(count, orient='index').reset_index()
    df = df.rename(columns={'index':'attribute', 0:'count'})
    return df

def test_task_func():
    obj1 = type('obj1', (object,), {'attr1': 'value1', 'attr2': 'value2'})
    obj2 = type('obj2', (object,), {'attr1': 'value1', 'attr2': 'value2'})
    obj3 = type('obj3', (object,), {'attr1': 'value3', 'attr2': 'value2'})
    obj_list = [obj1, obj2, obj3]

    # Test case 1: Valid attribute
    assert task_func(obj_list, 'attr1').equals(pd.DataFrame({'attribute': ['value1', 'value1', 'value3'], 'count': [2, 1, 1]}))

    # Test case 2: Invalid attribute
    with pytest.raises(AttributeError):
        task_func(obj_list, 'invalid_attr')

    # Test case 3: Empty object list
    assert task_func([], 'attr1').equals(pd.DataFrame())