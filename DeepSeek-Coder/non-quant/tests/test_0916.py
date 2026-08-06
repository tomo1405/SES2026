import pytest
from src_0916 import task_func
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'closing_price': [100, 102, 101, 104, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
    }
    df = pd.DataFrame(data)
    
    # Call the function
    outliers, ax = task_func(df)
    
    # Assertions to check the output
    assert len(outliers) > 0, "Expected at least one outlier"
    assert ax.get_title() == 'Outliers in Closing Prices', "Title should be 'Outliers in Closing Prices'"
    assert len(ax.lines) == 2, "Expected two lines in the plot"

    # Clean up
    plt.close()