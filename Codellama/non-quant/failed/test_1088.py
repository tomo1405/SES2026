import pytest
from src_1088 import task_func

def test_task_func():
    # Test with default values
    skewness, kurtosis, plot_paths = task_func()
    assert skewness == pytest.approx(0.0, abs=1e-3)
    assert kurtosis == pytest.approx(3.0, abs=1e-3)
    assert len(plot_paths) == 2
    assert "histogram_plot.png" in plot_paths
    assert "qq_plot.png" in plot_paths

    # Test with custom values
    skewness, kurtosis, plot_paths = task_func(mean=1000, std_dev=10)
    assert skewness == pytest.approx(0.0, abs=1e-3)
    assert kurtosis == pytest.approx(3.0, abs=1e-3)
    assert len(plot_paths) == 2
    assert "histogram_plot.png" in plot_paths
    assert "qq_plot.png" in plot_paths

    # Test with save_plots=True
    skewness, kurtosis, plot_paths = task_func(save_plots=True)
    assert skewness == pytest.approx(0.0, abs=1e-3)
    assert kurtosis == pytest.approx(3.0, abs=1e-3)
    assert len(plot_paths) == 2
    assert "histogram_plot.png" in plot_paths
    assert "qq_plot.png" in plot_paths
    assert os.path.exists(plot_paths[0])
    assert os.path.exists(plot_paths[1])