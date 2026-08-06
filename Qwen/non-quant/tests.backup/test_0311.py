import pytest
from src_0311 import task_func
import os
import csv
from statistics import mean

def test_task_func():
    # Define a temporary filename
    temp_filename = "test_people.csv"
    
    # Call the function to generate the CSV file
    filepath = task_func(temp_filename)
    
    # Check if the file exists
    assert os.path.exists(filepath), "The file was not created."
    
    # Read the contents of the file
    with open(filepath, newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check the header row
    assert rows[0] == ['Name', 'Age', 'Height', 'Weight'], "Header row is incorrect."
    
    # Check the number of people rows
    assert len(rows) == 101, "Incorrect number of rows in the CSV file."
    
    # Extract data rows and calculate averages
    data_rows = rows[1:-1]
    ages = [int(row[1]) for row in data_rows]
    heights = [int(row[2]) for row in data_rows]
    weights = [int(row[3]) for row in data_rows]
    
    # Check the average row
    averages = rows[-1]
    assert averages[0] == 'Average', "Average row label is incorrect."
    assert abs(float(averages[1]) - mean(ages)) < 1e-6, "Average age is incorrect."
    assert abs(float(averages[2]) - mean(heights)) < 1e-6, "Average height is incorrect."
    assert abs(float(averages[3]) - mean(weights)) < 1e-6, "Average weight is incorrect."
    
    # Clean up the temporary file
    os.remove(filepath)