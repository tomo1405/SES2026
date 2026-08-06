import pytest
from src_0311 import task_func
import os
import csv
from statistics import mean

def test_task_func():
    # Define a temporary filename for the CSV file
    temp_filename = 'test_people.csv'
    
    # Call the function to generate the CSV file
    filepath = task_func(temp_filename)
    
    # Check if the file was created
    assert os.path.exists(filepath), "The file was not created."
    
    # Read the contents of the file
    with open(filepath, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check the header
    assert rows[0] == ['Name', 'Age', 'Height', 'Weight'], "Header is incorrect."
    
    # Check the number of people entries
    assert len(rows[1:-1]) == 100, "Incorrect number of people entries."
    
    # Check the average row
    ages = [int(row[1]) for row in rows[1:-1]]
    heights = [int(row[2]) for row in rows[1:-1]]
    weights = [int(row[3]) for row in rows[1:-1]]
    
    expected_averages = [
        'Average',
        mean(ages),
        mean(heights),
        mean(weights)
    ]
    
    assert rows[-1] == expected_averages, "Average row is incorrect."
    
    # Clean up by removing the temporary file
    os.remove(filepath)