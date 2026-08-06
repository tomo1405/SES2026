import pytest
from src_0787 import task_func

def test_task_func_returns_dataframe():
    n = 10
    countries = ['USA', 'UK', 'China', 'India', 'Germany']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    output_path = None
    random_seed = None

    result = task_func(n, countries, products, output_path, random_seed)

    assert isinstance(result, pd.DataFrame)

def test_task_func_returns_correct_dataframe_shape():
    n = 10
    countries = ['USA', 'UK', 'China', 'India', 'Germany']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    output_path = None
    random_seed = None

    result = task_func(n, countries, products, output_path, random_seed)

    assert result.shape == (n, 3)

def test_task_func_returns_correct_dataframe_columns():
    n = 10
    countries = ['USA', 'UK', 'China', 'India', 'Germany']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    output_path = None
    random_seed = None

    result = task_func(n, countries, products, output_path, random_seed)

    assert result.columns.tolist() == ['Country', 'Product', 'Sales']

def test_task_func_returns_correct_dataframe_data():
    n = 10
    countries = ['USA', 'UK', 'China', 'India', 'Germany']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    output_path = None
    random_seed = None

    result = task_func(n, countries, products, output_path, random_seed)

    assert result['Country'].tolist() == ['USA', 'UK', 'China', 'India', 'Germany']
    assert result['Product'].tolist() == ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    assert result['Sales'].tolist() == [1, 2, 3, 4, 5]

def test_task_func_saves_data_to_csv_file():
    n = 10
    countries = ['USA', 'UK', 'China', 'India', 'Germany']
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    output_path = 'test_data.csv'
    random_seed = None

    task_func(n, countries, products, output_path, random_seed)

    with open(output_path, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    assert len(data) == n
    assert data[0]['Country'] == 'USA'
    assert data[0]['Product'] == 'Product A'
    assert data[0]['Sales'] == 1
    assert data[-1]['Country'] == 'Germany'
    assert data[-1]['Product'] == 'Product E'
    assert data[-1]['Sales'] == 5