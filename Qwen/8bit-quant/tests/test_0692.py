import pytest
from src_0692 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample DataFrame
    data = {
        'feature1': [1.0, 2.0, 3.0, 4.0],
        'feature2': [5.0, 6.0, 7.0, 8.0]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    labels = task_func(df)
    
    # Check that the output is a numpy array
    assert isinstance(labels, np.ndarray), "The output should be a numpy array"
    
    # Check that the length of the labels matches the number of rows in the input DataFrame
    assert len(labels) == df.shape[0], "The number of labels should match the number of rows in the input DataFrame"
    
    # Check that the labels are integers
    assert all(isinstance(label, int) for label in labels), "All labels should be integers"
    
    # Check that the labels are within the expected range (0 to n_clusters-1)
    assert set(labels) <= set(range(3)), "Labels should be within the range 0 to 2"