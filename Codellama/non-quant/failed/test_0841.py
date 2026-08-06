import pytest
from src_0841 import task_func

def test_task_func():
    file_path = 'test_data.csv'
    num_rows = 10
    data_dimensions = 5
    random_seed = 42

    result = task_func(file_path, num_rows, data_dimensions, random_seed)

    assert result == file_path

    df = pd.read_csv(file_path)
    assert df.shape == (num_rows, data_dimensions)
    assert df.columns.tolist() == [f'Feature_{i + 1}' for i in range(data_dimensions)]
    assert np.allclose(df.values, np.random.rand(num_rows, data_dimensions))