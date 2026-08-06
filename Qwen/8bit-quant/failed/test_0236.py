import pytest
from src_0236 import task_func
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def test_task_func_return_type():
    ax = task_func(mu=0, sigma=1)
    assert isinstance(ax, plt.Axes)

def test_task_func_histogram():
    ax = task_func(mu=0, sigma=1)
    lines = ax.get_lines()
    assert len(lines) == 2, "There should be two lines in the plot: one for the histogram fit and one for the quadratic model."

def test_task_func_histogram_fit():
    ax = task_func(mu=0, sigma=1)
    lines = ax.get_lines()
    histogram_fit_line = lines[0]
    xdata, ydata = histogram_fit_line.get_data()
    expected_ydata = 1 / (1 * np.sqrt(2 * np.pi)) * np.exp(- (xdata - 0)**2 / (2 * 1**2))
    np.testing.assert_array_almost_equal(ydata, expected_ydata, decimal=5)

def test_task_func_quadratic_model():
    ax = task_func(mu=0, sigma=1)
    lines = ax.get_lines()
    quadratic_model_line = lines[1]
    xdata, ydata = quadratic_model_line.get_data()
    model = ols('count ~ bins + np.power(bins, 2)', data={'count': np.histogram(xdata, bins=30, density=True)[0], 'bins': xdata}).fit()
    expected_ydata = model.params['Intercept'] + model.params['bins'] * xdata + model.params['np.power(bins, 2)'] * np.power(xdata, 2)
    np.testing.assert_array_almost_equal(ydata, expected_ydata, decimal=5)

def test_task_func_randomness():
    ax1 = task_func(mu=0, sigma=1, seed=0)
    ax2 = task_func(mu=0, sigma=1, seed=0)
    lines1 = ax1.get_lines()
    lines2 = ax2.get_lines()
    histogram_fit_line1 = lines1[0]
    histogram_fit_line2 = lines2[0]
    xdata1, ydata1 = histogram_fit_line1.get_data()
    xdata2, ydata2 = histogram_fit_line2.get_data()
    np.testing.assert_array_almost_equal(xdata1, xdata2)
    np.testing.assert_array_almost_equal(ydata1, ydata2)

def test_task_func_different_seed():
    ax1 = task_func(mu=0, sigma=1, seed=0)
    ax2 = task_func(mu=0, sigma=1, seed=1)
    lines1 = ax1.get_lines()
    lines2 = ax2.get_lines()
    histogram_fit_line1 = lines1[0]
    histogram_fit_line2 = lines2[0]
    xdata1, ydata1 = histogram_fit_line1.get_data()
    xdata2, ydata2 = histogram_fit_line2.get_data()
    with pytest.raises(AssertionError):
        np.testing.assert_array_almost_equal(xdata1, xdata2)
    with pytest.raises(AssertionError):
        np.testing.assert_array_almost_equal(ydata1, ydata2)