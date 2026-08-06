import seaborn as sns
from src_0308 import task_func


def test_task_func():
    # Test with a list of lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with an empty list
    list_of_lists = [[], [], []]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths
    list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [], [4, 5, 6], [7, 8, 9]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], []]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12], [13, 14, 15]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data

    # Test with a list of lists with different lengths and empty lists
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27], [28, 29, 30]]
    plot = task_func(list_of_lists)
    assert isinstance(plot, sns.histplot)
    assert plot.data == data