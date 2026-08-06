import random

import pytest
from src_1117 import task_func


# Mocking the random.randint function to control the output
class TestTaskFunc:
    @pytest.fixture
    def mock_random(self, monkeypatch):
        def mock_randint(a, b):
            return (a + b) // 2  # Always return the midpoint for simplicity
        monkeypatch.setattr(random, 'randint', mock_randint)

    def test_no_emp_department(self, mock_random):
        input_dict = {'HR': 5, 'ADMIN': 3}
        result = task_func(input_dict)
        assert result == (0, 0, [])

    def test_single_emp_department(self, mock_random):
        input_dict = {'EMP$$1': 1}
        result = task_func(input_dict)
        expected_mean = (AGE_RANGE[0] + AGE_RANGE[1]) / 2
        assert result == (expected_mean, expected_mean, [expected_mean])

    def test_multiple_emp_departments(self, mock_random):
        input_dict = {'EMP$$1': 2, 'EMP$$2': 3}
        result = task_func(input_dict)
        expected_mean = (AGE_RANGE[0] + AGE_RANGE[1]) / 2
        assert result == (expected_mean, expected_mean, [expected_mean])

    def test_empty_input(self, mock_random):
        input_dict = {}
        result = task_func(input_dict)
        assert result == (0, 0, [])

    def test_mode_with_duplicates(self, mock_random):
        input_dict = {'EMP$$1': 4}
        result = task_func(input_dict)
        expected_mean = (AGE_RANGE[0] + AGE_RANGE[1]) / 2
        assert result == (expected_mean, expected_mean, [expected_mean])