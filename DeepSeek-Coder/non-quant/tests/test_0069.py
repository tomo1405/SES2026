import pytest
from src_0069 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    # Mock data for testing
    data = pd.DataFrame({
        'Employee ID': ['EMP123', 'EMP456', 'EMP789'],
        'Age': [25, 30, 35]
    })

    # Call the function
    df, ax = task_func(data=data)

    # Assertions
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert len(df) == 2, "Expected 2 rows to be filtered"
    assert 'EMP' in df['Employee ID'].values, "Expected 'EMP' prefix to be filtered"
    assert ax is not None, "The histogram plot should be generated"

# Note: The assertion for the plot is more complex and typically involves checking the plot's properties,
# which can be done manually or through additional libraries like matplotlib's testing utilities.