import pytest
from src_1092 import task_func

def test_task_func():
    directory = 'data'
    path = os.path.join(directory, '*.txt')
    files = glob.glob(path)

    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                results.append(ast.literal_eval(line.strip()))

    assert results == task_func(directory)