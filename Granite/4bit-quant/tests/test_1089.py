import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: data is None
    data = None
    expected_output = pd.DataFrame(np.zeros((100, 5)), columns=[0, 1, 2, 3, 4])
    actual_output = task_func(data)
    assert actual_output.equals(expected_output)

    # Test case 2: data is not None
    data = np.random.rand(100, 5)
    df = pd.DataFrame(data)
    df[df < 0.5] = 0
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    expected_output = pd.DataFrame(scaled_data, columns=df.columns)
    actual_output = task_func(data)
    assert actual_output.equals(expected_output)

if __name__ == "__main__":
    pytest.main()