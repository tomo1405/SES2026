from src_0150 import task_func


def test_task_func_basic():
    elements = ['a', 'ab', 'abc']
    expected_columns = DEFAULT_COLUMNS
    result_df = task_func(elements)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.shape == (3, 2)
    assert result_df.iloc[0]['Element'] == 'a'
    assert result_df.iloc[0]['Count'] == 1
    assert result_df.iloc[1]['Element'] == 'ab'
    assert result_df.iloc[1]['Count'] == 2
    assert result_df.iloc[2]['Element'] == 'abc'
    assert result_df.iloc[2]['Count'] == 3

def test_task_func_with_index():
    elements = ['a', 'ab', 'abc']
    expected_columns = ['Index'] + DEFAULT_COLUMNS
    result_df = task_func(elements, include_index=True)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.shape == (3, 3)
    assert result_df.iloc[0]['Index'] == 0
    assert result_df.iloc[0]['Element'] == 'a'
    assert result_df.iloc[0]['Count'] == 1
    assert result_df.iloc[1]['Index'] == 1
    assert result_df.iloc[1]['Element'] == 'ab'
    assert result_df.iloc[1]['Count'] == 2
    assert result_df.iloc[2]['Index'] == 2
    assert result_df.iloc[2]['Element'] == 'abc'
    assert result_df.iloc[2]['Count'] == 3

def test_task_func_empty_list():
    elements = []
    expected_columns = DEFAULT_COLUMNS
    result_df = task_func(elements)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.shape == (0, 2)

def test_task_func_single_element():
    elements = ['single']
    expected_columns = DEFAULT_COLUMNS
    result_df = task_func(elements)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.shape == (1, 2)
    assert result_df.iloc[0]['Element'] == 'single'
    assert result_df.iloc[0]['Count'] == 6

def test_task_func_non_string_elements():
    elements = [1, 2.5, True]
    expected_columns = DEFAULT_COLUMNS
    result_df = task_func(elements)
    
    assert list(result_df.columns) == expected_columns
    assert result_df.shape == (3, 2)
    assert result_df.iloc[0]['Element'] == 1
    assert result_df.iloc[0]['Count'] == 1
    assert result_df.iloc[1]['Element'] == 2.5
    assert result_df.iloc[1]['Count'] == 3
    assert result_df.iloc[2]['Element'] == True
    assert result_df.iloc[2]['Count'] == 4