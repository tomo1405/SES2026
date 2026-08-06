python
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
PLOT_TITLE = 'Square root plot'
X_LABEL = 'x'
Y_LABEL = 'sqrt(x)'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def task_func(result):
    # Extract the 'from_user' values
    from_user_values = [d['from_user'] for d in result if 'from_user' in d]

    # Calculate the square roots
    square_roots = np.round(np.sqrt(from_user_values), 2)

    # Plot the square root function
    plt.figure()
    plt.plot(from_user_values, square_roots)
    plt.title(PLOT_TITLE)
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)

    # Annotate the plot with the current date and time
    now = datetime.now()
    now_str = now.strftime(TIME_FORMAT)
    plt.annotate(now_str, (0.05, 0.95), xycoords='axes fraction')
    ax = plt.gca()
    return square_roots, ax

# Test the function
def test_task_func():
    # Test case 1
    result = [{'from_user': 25}, {'from_user': 16}, {'from_user': 49}]
    expected_square_roots = [5.0, 4.0, 7.0]
    expected_ax = None
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax

    # Test case 2
    result = [{'from_user': 100}, {'from_user': 25}, {'from_user': 50}]
    expected_square_roots = [10.0, 5.0, 7.07]
    expected_ax = None
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax

    # Test case 3
    result = [{'from_user': 100}, {'from_user': 25}, {'from_user': 50}, {'from_user': 10}]
    expected_square_roots = [10.0, 5.0, 7.07, 3.16]
    expected_ax = None
    square_roots, ax = task_func(result)
    assert square_roots == expected_square_roots
    assert ax == expected_ax

test_task_func()