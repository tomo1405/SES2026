import numpy as np
from matplotlib.testing.decorators import check_figures_equal
from src_1066 import task_func


@check_figures_equal(extensions=["png"])
def test_task_func(fig_test, fig_ref):
    # Create a sample input array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Get the axes from the reference and test figures
    ax_ref = fig_ref.add_subplot()
    ax_test = fig_test.add_subplot()
    
    # Calculate the expected FFT coefficients manually
    row_sums = arr.sum(axis=1)
    fft_coefficients = np.fft.fft(row_sums)
    
    # Plot the expected FFT coefficients on the reference figure
    ax_ref.plot(np.abs(fft_coefficients))
    ax_ref.set_title("Absolute values of FFT coefficients")
    
    # Call the function under test
    task_func(arr)
    
    # The test figure should now have the same plot as the reference figure