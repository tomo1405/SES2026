import pytest
from src_0311 import task_func
import os
import csv
from statistics import mean

def test_task_func():
    # Define a temporary filename
    filename = "test_data.csv"
    
    # Call the function
    filepath = task_func(filename)
    
    # Check if the file was created
    assert os.path.exists(filepath), f"File {filepath} does not exist"
    
    # Read the contents of the file
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check the header
    assert rows[0] == ['Name', 'Age', 'Height', 'Weight'], "Header is incorrect"
    
    # Check the number of people
    assert len(rows) == 101, "Incorrect number of rows"
    
    # Check the last row (averages)
    ages = [int(row[1]) for row in rows[1:-1]]
    heights = [int(row[2]) for row in rows[1:-1]]
    weights = [int(row[3]) for row in rows[1:-1]]
    
    expected_averages = [
        'Average',
        round(mean(ages), 2),
        round(mean(heights), 2),
        round(mean(weights), 2)
    ]
    
    assert rows[-1] == expected_averages, "Averages are incorrect"
    
    # Clean up the file
    os.remove(filepath)