from datetime import datetime

import numpy as np
from src_0062 import task_func


def test_task_func():
    # Mock input data
    mock_result = [
        {'from_user': 4},
        {'from_user': 9},
        {'from_user': 16},
        {'from_user': 25}
    ]

    # Expected output
    expected_square_roots = np.array([2.0, 3.0, 4.0, 5.0])

    # Call the function
    square_roots, ax = task_func(mock_result)

    # Check if the calculated square roots are correct
    assert np.array_equal(square_roots, expected_square_roots), "The calculated square roots do not match the expected values."

    # Check if the plot has the correct title
    assert ax.get_title() == PLOT_TITLE, "The plot title does not match the expected value."

    # Check if the plot has the correct x-label
    assert ax.get_xlabel() == X_LABEL, "The x-label does not match the expected value."

    # Check if the plot has the correct y-label
    assert ax.get_ylabel() == Y_LABEL, "The y-label does not match the expected value."

    # Check if the annotation is present and correctly formatted
    annotations = [ann.get_text() for ann in ax.texts]
    now = datetime.now().strftime(TIME_FORMAT)
    assert now in annotations, "The annotation with the current date and time is missing or incorrect."

# To run the tests, use the command: pytest -v