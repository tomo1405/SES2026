import pytest
from src_0150 import task_func

def test_task_func_basic():
    elements = ['a', 'bb', 'ccc']
    result = task_func(elements)
    expected_df = pd.DataFrame({
        'Element': ['a', 'bb', 'ccc'],
        'Count': [1, 2, 3]
    })
    pd.testing.assert_frame_equal(result, expected_df)

def test_task_func_with_index():
    elements = ['a', 'bb', 'ccc']
    result = task_func(elements, include_index=True)
    expected_df = pd.DataFrame({
        'Index': [0, 1, 2],
        'Element': ['a', 'bb', 'ccc'],
        'Count': [1, 2, 3]
    })
    pd.testing.assert_frame_equal(result, expected_df)