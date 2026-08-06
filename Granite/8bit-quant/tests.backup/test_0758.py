import pytest
import numpy as np
import datetime
from src_0758 import task_func

def test_task_func():
    arr = np.array(['foo.bar.baz', 'abc.def.ghi', 'jkl.mno.pqr'])
    expected_result = np.array(['baz.bar.foo', 'ghi.def.abc', 'pqr.mno.jkl'])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_empty_array():
    arr = np.array([])
    expected_result = np.array([])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_single_element_array():
    arr = np.array(['foo.bar.baz'])
    expected_result = np.array(['baz.bar.foo'])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_multiple_dimensions_array():
    arr = np.array([['foo.bar.baz', 'abc.def.ghi'], ['jkl.mno.pqr', 'xyz. uv.wlm']])
    expected_result = np.array([['baz.bar.foo', 'ghi.def.abc'], ['pqr.mno.jkl', 'wlm. uv.xyz']])
    result = task_func(arr)
    assert np.array_equal(result, expected_result)

def test_task_func_with_datetime_now():
    arr = np.array(['foo.bar.baz'])
    expected_result = np.array(['baz.bar.foo'])
    original_now = datetime.datetime.now
    datetime.datetime.now = lambda: datetime.datetime(2023, 5, 1)
    result = task_func(arr)
    datetime.datetime.now = original_now
    assert np.array_equal(result, expected_result)