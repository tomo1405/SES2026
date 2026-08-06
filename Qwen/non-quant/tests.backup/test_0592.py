import pytest
from src_0592 import task_func
import pandas as pd
from unittest.mock import patch, MagicMock

@pytest.mark.parametrize("hours", [0, 1, 5])
def test_task_func_output(hours):
    with patch('src_0592.pd.DataFrame.to_csv') as mock_to_csv, \
         patch('src_0592.plt.show') as mock_show:
        
        file_path, ax = task_func(hours)
        
        assert file_path == 'custom_data.csv'
        assert isinstance(ax, MagicMock)

        # Check if to_csv was called with the correct parameters
        mock_to_csv.assert_called_once_with(file_path, index=False)
        
        # Check if plt.show was called
        mock_show.assert_called_once()

@pytest.mark.parametrize("hours", [0, 1, 5])
def test_task_func_dataframe_contents(hours):
    with patch('src_0592.pd.DataFrame.to_csv'), \
         patch('src_0592.plt.show'):
        
        _, _ = task_func(hours)
        
        df = pd.read_csv('custom_data.csv')
        
        assert len(df) == hours
        assert all(col in df.columns for col in ['Time', 'Temperature', 'Category'])

        # Validate Temperature and Category values
        for temp in df['Temperature']:
            assert -10 <= temp <= 40
        
        for category in df['Category']:
            assert category in ['Cold', 'Normal', 'Hot']

@pytest.mark.parametrize("temp, expected_category", [
    (-5, 'Cold'),
    (15, 'Normal'),
    (30, 'Hot')
])
def test_temperature_category_mapping(temp, expected_category):
    with patch('src_0592.pd.DataFrame.to_csv'), \
         patch('src_0592.plt.show'):
        
        with patch('src_0592.randint', return_value=temp):
            _, _ = task_func(1)
        
        df = pd.read_csv('custom_data.csv')
        
        assert df.iloc[0]['Category'] == expected_category