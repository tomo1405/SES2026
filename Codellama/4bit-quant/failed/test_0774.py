import pytest
from src_0774 import task_func

def test_task_func():
    # Set up test data
    source_dir = '/source/dir'
    target_dir = '/target/dir'
    file_pattern = re.compile(r'^(.*?)-\d+\.json$')
    filenames = ['file1-1.json', 'file2-2.json', 'file3-3.json']
    for filename in filenames:
        with open(os.path.join(source_dir, filename), 'w') as f:
            f.write('test data')

    # Run the function
    task_func()

    # Check the results
    for filename in filenames:
        prefix = file_pattern.match(filename).group(1)
        new_filename = f'{prefix}.json'
        assert os.path.exists(os.path.join(target_dir, new_filename))
        with open(os.path.join(target_dir, new_filename), 'r') as f:
            assert f.read() == 'test data'

    # Clean up
    for filename in filenames:
        os.remove(os.path.join(source_dir, filename))
        os.remove(os.path.join(target_dir, filename))