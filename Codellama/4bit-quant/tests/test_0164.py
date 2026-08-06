import numpy as np
import pandas as pd


def test_task_func():
    rows = 5
    cols = 5
    np.random.seed(0)
    categories = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame(np.random.rand(rows, cols) * 100, columns=categories[:cols])
    ax = data.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_ylabel('Value')
    ax.set_title('Stacked Bar Chart')

    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Stacked Bar Chart'
    assert ax.get_xlabel() == 'Category'
    assert ax.get_ylim() == (0, 100)
    assert ax.get_xlim() == (0, 5)
    assert ax.get_xticks() == np.arange(0, 5)
    assert ax.get_yticks() == np.arange(0, 100, 20)
    assert ax.get_xticklabels() == ['A', 'B', 'C', 'D', 'E']
    assert ax.get_yticklabels() == ['0', '20', '40', '60', '80', '100']

    assert len(ax.get_xticklabels()) == 5
    assert len(ax.get_yticklabels()) == 6

    assert ax.get_xticklabels()[0].get_text() == 'A'
    assert ax.get_yticklabels()[0].get_text() == '0'

    assert ax.get_xticklabels()[1].get_text() == 'B'
    assert ax.get_yticklabels()[1].get_text() == '20'

    assert ax.get_xticklabels()[2].get_text() == 'C'
    assert ax.get_yticklabels()[2].get_text() == '40'

    assert ax.get_xticklabels()[3].get_text() == 'D'
    assert ax.get_yticklabels()[3].get_text() == '60'

    assert ax.get_xticklabels()[4].get_text() == 'E'
    assert ax.get_yticklabels()[4].get_text() == '80'

    assert ax.get_xticklabels()[5].get_text() == 'F'
    assert ax.get_yticklabels()[5].get_text() == '100'