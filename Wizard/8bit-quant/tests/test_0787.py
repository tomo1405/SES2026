python
import pytest
from src_0787 import task_func

def test_task_func():
    # Test with default arguments
    df = task_func(10)
    assert df.shape == (10, 3)
    assert df['Country'].nunique() == 5
    assert df['Product'].nunique() == 5
    assert df['Sales'].min() >= 1
    assert df['Sales'].max() <= 100
    
    # Test with custom arguments
    df = task_func(5, countries=['A', 'B', 'C'], products=['X', 'Y', 'Z'], output_path='test.csv')
    assert df.shape == (5, 3)
    assert df['Country'].nunique() == 3
    assert df['Product'].nunique() == 3
    assert df['Sales'].min() >= 1
    assert df['Sales'].max() <= 100
    assert df.to_csv('test.csv', index=False) == 'Country,Product,Sales\nA,X,1\nA,Y,2\nA,Z,3\nB,X,4\nB,Y,5\nB,Z,6\nC,X,7\nC,Y,8\nC,Z,9\n'
    
    # Test with random seed
    df1 = task_func(10, random_seed=123)
    df2 = task_func(10, random_seed=123)
    assert df1.equals(df2)