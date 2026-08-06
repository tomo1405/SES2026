import pytest
from src_0267 import task_func

def test_task_func():
    my_path = 'path/to/directory'
    file_sizes = collections.defaultdict(int)

    for dirpath, dirnames, filenames in os.walk(my_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            file_sizes[f] += os.path.getsize(fp)

    with open(os.path.join(my_path, FILE_NAME), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'Size'])
        for row in file_sizes.items():
            writer.writerow(row)

    assert os.path.exists(os.path.join(my_path, FILE_NAME))
    assert os.path.isfile(os.path.join(my_path, FILE_NAME))
    assert os.path.getsize(os.path.join(my_path, FILE_NAME)) > 0