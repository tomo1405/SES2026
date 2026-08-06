import pytest
from src_0847 import task_func

class TestTaskFunc:
    def test_empty_list(self):
        assert task_func([], 'attr').empty

    def test_single_object(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj = Dummy('value')
        result = task_func([obj], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value'], 'count': [1]})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_multiple_objects_same_attr(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj1 = Dummy('value')
        obj2 = Dummy('value')
        result = task_func([obj1, obj2], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value'], 'count': [2]})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_multiple_objects_different_attrs(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj1 = Dummy('value1')
        obj2 = Dummy('value2')
        result = task_func([obj1, obj2], 'attr')
        expected_df = pd.DataFrame({'attribute': ['value1', 'value2'], 'count': [1, 1]})
        pd.testing.assert_frame_equal(result, expected_df)

    def test_nonexistent_attribute(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj = Dummy('value')
        with pytest.raises(AttributeError):
            task_func([obj], 'nonexistent_attr')

    def test_mixed_types(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj1 = Dummy('value1')
        obj2 = 42
        with pytest.raises(AttributeError):
            task_func([obj1, obj2], 'attr')