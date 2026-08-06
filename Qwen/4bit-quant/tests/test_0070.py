import io
import random

import matplotlib.pyplot as plt
from src_0070 import task_func


def test_task_func():
    # Mocking the random number generation to ensure predictability
    class MockRandom:
        def randint(self, a, b):
            return (a + b) // 2

    random_instance = MockRandom()
    original_random = random.random
    random.random = lambda: 0.5  # Ensuring consistent results for plt.hist
    random.randint = random_instance.randint

    # Prepare test data
    test_data = {
        'EMPXX1': 5,
        'EMPXX2': 3,
        'NOTEMPXX': 2
    }

    # Capture the plot output
    fig, ax = plt.subplots()
    captured_output = io.BytesIO()
    plt.savefig(captured_output, format='png')
    plt.close(fig)

    # Call the function
    result_ax = task_func(test_data)

    # Check if the returned axis is the same as the one used for plotting
    assert result_ax == ax

    # Restore the original random module functions
    random.random = original_random
    random.randint = original_random.randint