import pytest
from src_1065 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample 2D array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Call the function
    ax = task_func(arr)
    
    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib AxesSubplot object"
    
    # Check if the title is set correctly
    assert ax.get_title() == "Heatmap of the 2D Array", "The title of the heatmap should be 'Heatmap of the 2D Array'"
    
    # Check if the heatmap is annotated
    annotations = [text.get_text() for text in ax.texts]
    expected_annotations = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    assert annotations == expected_annotations, "The heatmap should be annotated with the correct values"
    
    # Check if vmax and vmin are set correctly
    assert ax.collections[0].get_array().max() == np.max(arr), "vmax should be set to the maximum value in the array"
    assert ax.collections[0].get_array().min() == np.min(arr), "vmin should be set to the minimum value in the array"

# Run the tests
if __name__ == "__main__":
    pytest.main()