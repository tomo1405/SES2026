import pytest
from src_0849 import task_func

class TestTaskFunc:
    def test_empty_list(self):
        result = task_func([], 'attr')
        assert result == ([], None)

    def test_single_element(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj_list = [Dummy(10)]
        result = task_func(obj_list, 'attr')
        assert result == ([10], 10)

    def test_multiple_elements(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj_list = [Dummy(1), Dummy(3), Dummy(2), Dummy(5), Dummy(4)]
        result = task_func(obj_list, 'attr', top_n=3)
        assert result[0] == [5, 4, 3]
        assert result[1] in [1, 2, 3, 4, 5]

    def test_top_n_greater_than_list_length(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj_list = [Dummy(1), Dummy(2)]
        result = task_func(obj_list, 'attr', top_n=5)
        assert result[0] == [2, 1]
        assert result[1] in [1, 2]

    def test_with_seed(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj_list = [Dummy(1), Dummy(2), Dummy(3)]
        result1 = task_func(obj_list, 'attr', seed=42)
        result2 = task_func(obj_list, 'attr', seed=42)
        assert result1 == result2

    def test_invalid_attribute(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj_list = [Dummy(1)]
        with pytest.raises(AttributeError):
            task_func(obj_list, 'non_existent_attr')

    def test_non_numeric_attribute(self):
        class Dummy:
            def __init__(self, attr):
                self.attr = attr

        obj_list = [Dummy('a'), Dummy('b'), Dummy('c')]
        result = task_func(obj_list, 'attr', top_n=2)
        assert result[0] == ['c', 'b']
        assert result[1] in ['a', 'b', 'c']