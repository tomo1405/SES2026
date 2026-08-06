import pytest
from src_0152 import task_func

def test_task_func():
    # Test case 1: Normal case
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    data_keys = ['a', 'b', 'c']
    expected_df = pd.DataFrame({'a': [0.5, 0.6666666666666666, 0.8333333333333334],
                              'b': [0.6666666666666666, 0.8333333333333334, 1.0],
                              'c': [0.8333333333333334, 1.0, 1.0]})
    expected_ax = expected_df.plot(kind='line')
    expected_ax.set_title('Normalized Data')
    expected_ax.set_ylabel('Normalized Value')
    expected_ax.set_xlabel('Index')

    normalized_df, ax = task_func(data_dict, data_keys)

    assert normalized_df.equals(expected_df)
    assert ax.get_title() == 'Normalized Data'
    assert ax.get_ylabel() == 'Normalized Value'
    assert ax.get_xlabel() == 'Index'

    # Test case 2: Empty data dictionary
    data_dict = {}
    data_keys = ['a', 'b', 'c']

    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)

    # Test case 3: Empty keys list
    data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    data_keys = []

    with pytest.raises(ValueError):
        task_func(data_dict, data_keys)