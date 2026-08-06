import pytest
from src_0112 import task_func

def test_task_func():
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                      'Time': ['12:00', '13:00', '14:00'],
                      'Temperature': [20, 22, 24]})
    ax = task_func(df)
    assert isinstance(ax, sns.heatmap)
    assert ax.get_title() == 'Temperature Heatmap'
    assert ax.get_xlabel() == 'Month'
    assert ax.get_ylabel() == 'Day'
    assert ax.get_zlabel() == 'Temperature'
    assert ax.get_xticklabels() == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    assert ax.get_yticklabels() == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    assert ax.get_zlim() == (0, 24)