import pytest
from src_0165 import task_func

def test_task_func():
    num_labels = 5
    data_range = (0, 1)
    expected_columns = [f'Label{i + 1}' for i in range(num_labels)]
    expected_data = pd.DataFrame(np.random.uniform(data_range[0], data_range[1], size=(num_labels, num_labels)), columns=expected_columns)

    fig = task_func(num_labels, data_range)
    ax = fig.axes[0]

    assert ax.get_title() == 'Stacked Bar Plot'
    assert ax.get_xlabel() == 'Label'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_xticks() == expected_columns
    assert ax.get_yticks() == np.arange(0, 1.1, 0.1)
    assert ax.get_xticklabels() == expected_columns
    assert ax.get_yticklabels() == [f'{i:.1f}' for i in np.arange(0, 1.1, 0.1)]
    assert ax.get_legend().get_title().get_text() == 'Label'
    assert ax.get_legend().get_texts() == expected_columns
    assert ax.get_legend().get_patches()[0].get_facecolor() == 'blue'
    assert ax.get_legend().get_patches()[1].get_facecolor() == 'red'
    assert ax.get_legend().get_patches()[2].get_facecolor() == 'green'
    assert ax.get_legend().get_patches()[3].get_facecolor() == 'yellow'
    assert ax.get_legend().get_patches()[4].get_facecolor() == 'orange'