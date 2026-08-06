import pytest
from src_0062 import task_func
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def test_task_func():
    # Mock input data
    result = [
        {'from_user': 4},
        {'from_user': 9},
        {'from_user': 16},
        {'from_user': 25}
    ]

    # Expected output
    expected_square_roots = np.array([2.0, 3.0, 4.0, 5.0])

    # Call the function
    square_roots, ax = task_func(result)

    # Check if the square roots are calculated correctly
    assert np.array_equal(square_roots, expected_square_roots)

    # Check if the plot title is correct
    assert ax.get_title() == 'Square root plot'

    # Check if the x and y labels are correct
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'sqrt(x)'

    # Check if the annotation is present and in the correct format
    annotations = ax.texts
    assert len(annotations) == 1
    annotation_text = annotations[0].get_text()
    try:
        datetime.strptime(annotation_text, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        pytest.fail("Annotation is not in the correct datetime format")

    # Close the plot to avoid displaying it during testing
    plt.close(ax.figure)