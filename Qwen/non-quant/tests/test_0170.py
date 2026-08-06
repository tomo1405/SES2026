import base64
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0170 import task_func


def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_sigma_value():
    with pytest.raises(ValueError):
        task_func(np.array([[1, 2], [3, 4]]), sigma=-1)

def test_task_func_output():
    image = np.array([[1, 2], [3, 4]])
    ax, filtered_image = task_func(image)
    
    assert isinstance(ax, plt.AxesSubplot)
    assert isinstance(filtered_image, np.ndarray)
    assert filtered_image.shape == image.shape

def test_task_func_plot_titles():
    image = np.array([[1, 2], [3, 4]])
    ax, _ = task_func(image)
    
    assert ax[0].get_title() == 'Original'
    assert ax[1].get_title() == 'Filtered'

def test_task_func_plot_images():
    image = np.array([[1, 2], [3, 4]])
    ax, _ = task_func(image)
    
    original_image = ax[0].images[0].get_array()
    filtered_image = ax[1].images[0].get_array()
    
    assert np.array_equal(original_image, image)
    assert np.array_equal(filtered_image, gaussian_filter(image, sigma=2))

def test_task_func_plot_saving():
    image = np.array([[1, 2], [3, 4]])
    ax, _ = task_func(image)
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    # This is a basic check to ensure the plot was saved correctly.
    # A more thorough check would involve image comparison or analysis.
    assert len(img_str) > 0