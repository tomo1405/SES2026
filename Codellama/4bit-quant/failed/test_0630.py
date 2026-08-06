import pytest
from src_0630 import task_func

def test_task_func():
    dataset = [
        pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}),
        pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
    ]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    assert os.path.exists(output_dir)
    assert os.path.isdir(output_dir)
    assert os.path.exists(os.path.join(output_dir, filename))
    assert os.path.isfile(os.path.join(output_dir, filename))

    with open(os.path.join(output_dir, filename), 'r') as f:
        lines = f.readlines()
        assert len(lines) == 4
        assert lines[0] == 'A,B\n'
        assert lines[1] == '1,4\n'
        assert lines[2] == '------\n'
        assert lines[3] == '7,10\n'