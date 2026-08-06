import pandas as pd
import pytest
from src_0847 import task_func


class TestTaskFunc:

    def test_empty_list(self):
        result = task_func([], 'attr')
        assert result.empty

    def test_single_object(self):
        class MockObj:
            def __init__(self, attr):
                self.attr = attr

        obj = MockObj('value1')
        result = task_func([obj], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1'], 'count': [1]})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_multiple_objects_same_attr(self):
        class MockObj:
            def __init__(self, attr):
                self.attr = attr

        obj1 = MockObj('value1')
        obj2 = MockObj('value1')
        result = task_func([obj1, obj2], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1'], 'count': [2]})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_multiple_objects_different_attrs(self):
        class MockObj:
            def __init__(self, attr):
                self.attr = attr

        obj1 = MockObj('value1')
        obj2 = MockObj('value2')
        result = task_func([obj1, obj2], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1', 'value2'], 'count': [1, 1]})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_nonexistent_attribute(self):
        class MockObj:
            def __init__(self, attr):
                self.attr = attr

        obj = MockObj('value1')
        with pytest.raises(AttributeError):
            task_func([obj], 'nonexistent_attr')

    def test_mixed_types(self):
        class MockObj1:
            def __init__(self, attr):
                self.attr = attr

        class MockObj2:
            def __init__(self, attr):
                self.attr = attr

        obj1 = MockObj1('value1')
        obj2 = MockObj2('value2')
        result = task_func([obj1, obj2], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1', 'value2'], 'count': [1, 1]})
        pd.testing.assert_frame_equal(result, expected_df)