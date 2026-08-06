import os

from src_0630 import task_func


def test_task_func():
    dataset = [df1, df2, df3]  # Replace df1, df2, and df3 with your actual DataFrame objects
    filename = 'output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    assert os.path.exists(os.path.join(output_dir, filename))

    with open(os.path.join(output_dir, filename), 'r') as f:
        content = f.read()
        assert '------' in content
        assert '\n' in content