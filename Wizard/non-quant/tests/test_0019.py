python
import subprocess
import csv
import glob
import random
import os

def task_func(file):
    # Check if file exists
    if not os.path.exists(file):
        print("Provided file does not exist.")
        return []
    
    # Check for CSV file extension
    if not file.endswith('.csv'):
        print("Provided file is not a CSV.")
        return []

    try:
        subprocess.call(['split', '-n', '5', '-d', file, 'split_'])
        split_files = glob.glob('split_*')

        for split_file in split_files:
            with open(split_file, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)

            random.shuffle(rows)

            with open(split_file, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(rows)

        return split_files
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Test the function with a valid CSV file
def test_task_func_valid_csv():
    file = 'test.csv'
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['col1', 'col2', 'col3'])
        writer.writerow(['1', '2', '3'])
        writer.writerow(['4', '5', '6'])
        writer.writerow(['7', '8', '9'])
        writer.writerow(['10', '11', '12'])

    split_files = task_func(file)
    assert len(split_files) == 5
    for split_file in split_files:
        with open(split_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        assert len(rows) == 2

    os.remove(file)
    for split_file in split_files:
        os.remove(split_file)

# Test the function with an invalid file
def test_task_func_invalid_file():
    file = 'invalid.txt'
    split_files = task_func(file)
    assert split_files == []

# Test the function with a non-CSV file
def test_task_func_non_csv():
    file = 'test.txt'
    with open(file, 'w') as f:
        f.write('This is not a CSV file.')

    split_files = task_func(file)
    assert split_files == []

    os.remove(file)