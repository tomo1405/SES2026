import pytest
from src_0837 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    csv_dir = tempfile.mkdtemp()
    processed_dir = tempfile.mkdtemp()
    yield csv_dir, processed_dir
    shutil.rmtree(csv_dir)
    shutil.rmtree(processed_dir)

@pytest.fixture
def create_csv_files(csv_dir):
    data1 = [['332', 'data1'], ['444', 'data2']]
    data2 = [['555', 'data3'], ['332', 'data4']]

    with open(os.path.join(csv_dir, 'file1.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data1)

    with open(os.path.join(csv_dir, 'file2.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data2)

@pytest.mark.parametrize("simulate", [True, False])
def test_task_func(setup_directories, create_csv_files, simulate):
    csv_dir, processed_dir = setup_directories

    expected_result = {'file1.csv': 0}
    if not simulate:
        expected_result['file2.csv'] = 1

    result = task_func(target_value='332', csv_dir=csv_dir, processed_dir=processed_dir, simulate=simulate)

    assert result == expected_result

    if not simulate:
        assert not os.path.exists(os.path.join(csv_dir, 'file1.csv'))
        assert not os.path.exists(os.path.join(csv_dir, 'file2.csv'))
        assert os.path.exists(os.path.join(processed_dir, 'file1.csv'))
        assert os.path.exists(os.path.join(processed_dir, 'file2.csv'))
    else:
        assert os.path.exists(os.path.join(csv_dir, 'file1.csv'))
        assert os.path.exists(os.path.join(csv_dir, 'file2.csv'))
        assert not os.path.exists(os.path.join(processed_dir, 'file1.csv'))
        assert not os.path.exists(os.path.join(processed_dir, 'file2.csv'))