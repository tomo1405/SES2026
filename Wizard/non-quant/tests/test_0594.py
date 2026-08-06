python
import csv
import os
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
# Constants
VEHICLE_TYPES = ['Car', 'Bus', 'Truck', 'Bike']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    FILE_PATH = os.path.join(output_dir, 'traffic_data.csv')
    data = [['Time'] + VEHICLE_TYPES]
    for i in range(hours):
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')] + [randint(0, 50) for _ in VEHICLE_TYPES]
        data.append(row)

    with open(FILE_PATH, 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    df = pd.read_csv(FILE_PATH)

    if df.empty:
        return FILE_PATH, None

    ax = df.plot(x='Time', y=VEHICLE_TYPES, kind='line', title='Traffic Data Over Time')
    plt.xlabel('Time')
    plt.ylabel('Vehicle Count')
    plt.tight_layout()
    plt.show()

    return FILE_PATH, ax

# Test Cases
def test_task_func_default():
    file_path, ax = task_func(10)
    assert os.path.exists(file_path)
    assert ax is not None

def test_task_func_custom_output_dir():
    file_path, ax = task_func(10, output_dir='./custom_output')
    assert os.path.exists(file_path)
    assert ax is not None

def test_task_func_empty_dataframe():
    file_path, ax = task_func(0)
    assert os.path.exists(file_path)
    assert ax is None