import pytest
from src_1055 import task_func

def test_task_func():
    file_path = "test_data.csv"
    mean, std_dev, ax = task_func(file_path)
    assert isinstance(mean, float)
    assert isinstance(std_dev, float)
    assert isinstance(ax, matplotlib.axes.Axes)

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        population = [int(row[0]) for row in reader]

    sample = np.random.choice(population, 30, replace=False)
    assert np.allclose(mean, np.mean(sample))
    assert np.allclose(std_dev, np.std(sample, ddof=1))

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mean, std_dev)
    assert np.allclose(p, ax.get_ydata())

    assert ax.get_xlabel() == "Sample Values"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Sample Histogram with Normal Distribution Overlay"