import os
import shutil
import csv
from src_0837 import task_func

def test_task_func():
    # Test case 1: target_value is found in the first row of a CSV file
    csv_file = 'test1.csv'
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['332', 'Test', 'Data'])
    result = task_func(target_value='332', csv_dir='.', simulate=True)
    assert result == {csv_file: 0}
    os.remove(csv_file)

    # Test case 2: target_value is not found in any CSV file
    result = task_func(target_value='42', csv_dir='.', simulate=True)
    assert result == {}

    # Test case 3: target_value is found in multiple CSV files
    csv_files = ['test2_1.csv', 'test2_2.csv']
    for file in csv_files:
        with open(file, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['42', 'Test', 'Data'])
    result = task_func(target_value='42', csv_dir='.', simulate=True)
    assert result == {file: 0 for file in csv_files}
    for file in csv_files:
        os.remove(file)

    # Test case 4: simulate=False
    csv_file = 'test4.csv'
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['332', 'Test', 'Data'])
    result = task_func(target_value='332', csv_dir='.', processed_dir='.', simulate=False)
    assert result == {csv_file: 0}
    assert os.path.exists('.\\processed_files\\' + csv_file)
    os.remove(csv_file)
    os.remove('.\\processed_files\\' + csv_file)