import pytest
from src_0847 import task_func
import pandas as pd
from collections import Counter

class TestTaskFunc:

    def test_empty_list(self):
        result = task_func([], 'attr')
        assert result.equals(pd.DataFrame())

    def test_single_object(self):
        class MockObj:
            def __init__(self, attr_value):
                self.attr = attr_value

        obj1 = MockObj('value1')
        result = task_func([obj1], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1'], 'count': [1]})
        assert result.equals(expected_df)

    def test_multiple_objects_same_attr(self):
        class MockObj:
            def __init__(self, attr_value):
                self.attr = attr_value

        obj1 = MockObj('value1')
        obj2 = MockObj('value1')
        obj3 = MockObj('value1')
        result = task_func([obj1, obj2, obj3], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1'], 'count': [3]})
        assert result.equals(expected_df)

    def test_multiple_objects_different_attrs(self):
        class MockObj:
            def __init__(self, attr_value):
                self.attr = attr_value

        obj1 = MockObj('value1')
        obj2 = MockObj('value2')
        obj3 = MockObj('value3')
        result = task_func([obj1, obj2, obj3], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1', 'value2', 'value3'], 'count': [1, 1, 1]})
        assert result.equals(expected_df)

    def test_mixed_attributes(self):
        class MockObj:
            def __init__(self, attr_value):
                self.attr = attr_value

        obj1 = MockObj('value1')
        obj2 = MockObj('value1')
        obj3 = MockObj('value2')
        result = task_func([obj1, obj2, obj3], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1', 'value2'], 'count': [2, 1]})
        assert result.equals(expected_df)

    def test_nonexistent_attribute(self):
        class MockObj:
            def __init__(self):
                pass

        obj1 = MockObj()
        with pytest.raises(AttributeError):
            task_func([obj1], 'nonexistent_attr')

    def test_none_values(self):
        class MockObj:
            def __init__(self, attr_value):
                self.attr = attr_value

        obj1 = MockObj(None)
        obj2 = MockObj(None)
        obj3 = MockObj('value1')
        result = task_func([obj1, obj2, obj3], 'attr')
        expected_df = pd.DataFrame({'attribute': [None, 'value1'], 'count': [2, 1]})
        assert result.equals(expected_df)