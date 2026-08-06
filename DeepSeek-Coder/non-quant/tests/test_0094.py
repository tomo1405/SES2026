import pytest
from src_0094 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def test_task_func():
    # Test with valid input
    data = np.array([[1, 2], [3, 4], [5, 6]])
    expected_output = (pd.DataFrame({
        'PC1': [-2.82842712474619, -0.615363104325068, 2.44948974278378],
                             'PC2': [-0.472455591362522, -1.230726208650136, 0.777123812334545]
    }), None)
    result = task_func(data)
    assert result == expected_output

    # Add more test cases as needed

    # Add more tests to cover different scenarios