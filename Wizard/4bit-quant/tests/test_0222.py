python
import pandas as pd
import numpy as np
import scipy.stats as stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def test_task_func():
    # Test case 1
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [6, 7, 8, 9, 10], 'feature3': [11, 12, 13, 14, 15], 'feature4': [16, 17, 18, 19, 20], 'feature5': [21, 22, 23, 24, 25]})
    dct = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500}
    expected_statistics = {'feature1': {'mean': 3.0, 'median': 3.0, 'mode': 3.0, 'variance': 6.666666666666667}, 'feature2': {'mean': 8.0, 'median': 8.0, 'mode': 8.0, 'variance': 8.0}, 'feature3': {'mean': 13.0, 'median': 13.0, 'mode': 13.0, 'variance': 10.666666666666666}, 'feature4': {'mean': 18.0, 'median': 18.0, 'mode': 18.0, 'variance': 12.0}, 'feature5': {'mean': 23.0, 'median': 23.0, 'mode': 23.0, 'variance': 12.666666666666666}}
    assert task_func(df, dct) == expected_statistics
    
    # Test case 2
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [6, 7, 8, 9, 10], 'feature3': [11, 12, 13, 14, 15], 'feature4': [16, 17, 18, 19, 20], 'feature5': [21, 22, 23, 24, 25]})
    dct = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500, '6': 600}
    expected_statistics = "Invalid input"
    assert task_func(df, dct) == expected_statistics
    
    # Test case 3
    df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5], 'feature2': [6, 7, 8, 9, 10], 'feature3': [11, 12, 13, 14, 15], 'feature4': [16, 17, 18, 19, 20], 'feature5': [21, 22, 23, 24, 25]})
    dct = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500, '6': 600, '7': 700}
    expected_statistics = "Invalid input"
    assert task_func(df, dct) == expected_statistics