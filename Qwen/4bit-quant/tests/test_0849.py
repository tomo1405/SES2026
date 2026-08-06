import pytest
from src_0849 import task_func

class TestTaskFunc:
    def test_empty_list(self):
        result, random_value = task_func([], 'attr')
        assert result == []
        assert random_value is None

    def test_single_element(self):
        class MockObj:
            def __init__(self, value):
                self.attr = value

        obj = MockObj(10)
        result, random_value = task_func([obj], 'attr')
        assert result == [10]
        assert random_value == 10

    def test_multiple_elements(self):
        class MockObj:
            def __init__(self, value):
                self.attr = value

        obj1 = MockObj(10)
        obj2 = MockObj(20)
        obj3 = MockObj(15)
        obj4 = MockObj(5)
        obj5 = MockObj(25)
        obj6 = MockObj(30)

        result, random_value = task_func([obj1, obj2, obj3, obj4, obj5, obj6], 'attr', top_n=3)
        assert result == [30, 25, 20]
        assert random_value in [10, 15, 20, 25, 30]

    def test_with_seed(self):
        class MockObj:
            def __init__(self, value):
                self.attr = value

        obj1 = MockObj(10)
        obj2 = MockObj(20)
        obj3 = MockObj(15)
        obj4 = MockObj(5)
        obj5 = MockObj(25)
        obj6 = MockObj(30)

        result1, random_value1 = task_func([obj1, obj2, obj3, obj4, obj5, obj6], 'attr', top_n=3, seed=42)
        result2, random_value2 = task_func([obj1, obj2, obj3, obj4, obj5, obj6], 'attr', top_n=3, seed=42)

        assert result1 == result2
        assert random_value1 == random_value2

    def test_attr_not_exist(self):
        class MockObj:
            def __init__(self, value):
                self.another_attr = value

        obj1 = MockObj(10)
        with pytest.raises(AttributeError):
            task_func([obj1], 'attr')

    def test_non_numeric_attr(self):
        class MockObj:
            def __init__(self, value):
                self.attr = value

        obj1 = MockObj('a')
        obj2 = MockObj('b')
        obj3 = MockObj('c')

        result, random_value = task_func([obj1, obj2, obj3], 'attr', top_n=2)
        assert result == ['c', 'b']
        assert random_value in ['a', 'b', 'c']