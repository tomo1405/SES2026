import pytest
from src_0379 import task_func

def test_task_func_valid_data():
    data_dir = './data/'
    data_files = ['file1.csv', 'file2.csv']
    summary_data = [[os.path.basename(file), data.shape[0], data.shape[1]] for file in data_files]
    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    expected_output = table.draw()

    with pytest.raises(FileNotFoundError):
        task_func(data_dir)

    with pytest.raises(ValueError):
        task_func(data_dir)

    with pytest.raises(pd.errors.EmptyDataError):
        task_func(data_dir)

    assert task_func(data_dir) == expected_output