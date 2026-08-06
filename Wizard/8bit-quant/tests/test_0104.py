python
import pytest
import pandas as pd
import matplotlib.pyplot as plt

def task_func(temperatures):
    try:
        if temperatures.empty or not isinstance(temperatures, pd.DataFrame):
            raise ValueError("Input temperatures must be a non-empty pandas DataFrame.")

        # Setting the font to Arial
        font = {'sans-serif': 'Arial', 'family': 'sans-serif'}
        plt.rc('font', **font)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(temperatures.index, temperatures['temperature'])
        ax.set_xlabel('Date')
        ax.set_ylabel('Temperature (°C)')
        ax.set_title('Daily Temperatures in New York')

        return ax

    except Exception as e:
        raise ValueError(f"An error occurred: {e}")

def test_task_func():
    # Test case 1: Valid input
    temperatures = pd.DataFrame({'temperature': [10, 15, 20, 25, 30]}, index=['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'])
    ax = task_func(temperatures)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Empty input
    temperatures = pd.DataFrame()
    with pytest.raises(ValueError) as e:
        task_func(temperatures)
    assert str(e.value) == "Input temperatures must be a non-empty pandas DataFrame."

    # Test case 3: Non-DataFrame input
    temperatures = [10, 15, 20, 25, 30]
    with pytest.raises(ValueError) as e:
        task_func(temperatures)
    assert str(e.value) == "Input temperatures must be a non-empty pandas DataFrame."

    # Test case 4: Error handling
    temperatures = pd.DataFrame({'temperature': [10, 15, 20, 25, 30]}, index=['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'])
    with pytest.raises(ValueError) as e:
        task_func(temperatures)
    assert str(e.value) == "An error occurred: Input temperatures must be a non-empty pandas DataFrame."