import pytest
from src_0389 import task_func

def test_task_func():
    my_tuple = ('a', 'b', 'c')
    path_csv_files = ['file1.csv', 'file2.csv']

    counter = task_func(my_tuple, path_csv_files)

    assert isinstance(counter, dict)
    assert all(isinstance(value, collections.Counter) for value in counter.values())
    assert all(key in counter for key in my_tuple)

    for csv_file in path_csv_files:
        df = pd.read_csv(csv_file)

        for column in my_tuple:
            if column in df:
                assert counter[column].most_common() == df[column].value_counts().to_dict().items()