import pytest
from src_0849 import task_func

class TestTaskFunc:
    def test_with_valid_data(self):
        class Dummy:
            def __init__(self, value):
                self.value = value

        obj_list = [Dummy(10), Dummy(20), Dummy(30), Dummy(40), Dummy(50)]
        top_values, random_value = task_func(obj_list, 'value')
        assert top_values == [50, 40, 30, 20, 10]
        assert random_value in [10, 20, 30, 40, 50]

    def test_with_top_n_greater_than_list_length(self):
        class Dummy:
            def __init__(self, value):
                self.value = value

        obj_list = [Dummy(10), Dummy(20)]
        top_values, random_value = task_func(obj_list, 'value', top_n=5)
        assert top_values == [20, 10]
        assert random_value in [10, 20]

    def test_with_empty_list(self):
        class Dummy:
            def __init__(self, value):
                self.value = value

        obj_list = []
        top_values, random_value = task_func(obj_list, 'value')
        assert top_values == []
        assert random_value is None

    def test_with_seed(self):
        class Dummy:
            def __init__(self, value):
                self.value = value

        obj_list = [Dummy(10), Dummy(20), Dummy(30)]
        top_values, random_value = task_func(obj_list, 'value', seed=42)
        assert top_values == [30, 20, 10]
        assert random_value == 20  # Deterministic with seed 42

    def test_with_nonexistent_attribute(self):
        class Dummy:
            def __init__(self, value):
                self.value = value

        obj_list = [Dummy(10), Dummy(20)]
        with pytest.raises(AttributeError):
            task_func(obj_list, 'nonexistent_attr')

    def test_with_non_numeric_attribute(self):
        class Dummy:
            def __init__(self, value):
                self.value = value

        obj_list = [Dummy('a'), Dummy('b'), Dummy('c')]
        top_values, random_value = task_func(obj_list, 'value')
        assert top_values == ['c', 'b', 'a']
        assert random_value in ['a', 'b', 'c']