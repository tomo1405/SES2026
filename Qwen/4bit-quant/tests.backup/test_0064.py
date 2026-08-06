import pytest
from src_0064 import task_func

def test_task_func():
    car_dict = {'Car1': 'Red', 'Car2': 'Blue', 'Car3': 'Red', 'Car4': 'Green'}
    df, ax = task_func(car_dict)
    
    # Check if DataFrame is created correctly
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['Car', 'Color']
    assert len(df) == 4
    
    # Check if the DataFrame has the correct data
    expected_data = [
        ('Car1', 'Red'),
        ('Car2', 'Blue'),
        ('Car3', 'Red'),
        ('Car4', 'Green')
    ]
    assert all(df.iloc[i].tolist() == expected_data[i] for i in range(len(df)))
    
    # Check if the axes object is returned
    assert isinstance(ax, plt.Axes)