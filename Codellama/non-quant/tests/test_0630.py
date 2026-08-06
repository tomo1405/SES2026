import os

import pandas as pd
from src_0630 import task_func


def test_task_func():
    dataset = [
        pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}),
        pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]}),
        pd.DataFrame({'a': [13, 14, 15], 'b': [16, 17, 18]}),
    ]
    filename = 'test_output.csv'
    output_dir = './output'

    task_func(dataset, filename, output_dir)

    with open(os.path.join(output_dir, filename), 'r') as f:
        content = f.read()

    assert '------\n' in content
    assert 'a,b\n1,4\n2,5\n3,6\n' in content
    assert 'a,b\n7,10\n8,11\n9,12\n' in content
    assert 'a,b\n13,16\n14,17\n15,18\n' in content