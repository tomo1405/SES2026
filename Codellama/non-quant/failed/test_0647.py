import pytest
from src_0647 import task_func

def test_task_func_valid_csv_path():
    csv_path = os.path.join(OUTPUT_DIR, 'data.csv')
    date_column = 'date'
    df = pd.DataFrame({'date': ['2022-01-01', '2022-01-02', '2022-01-03']})
    df.to_csv(csv_path, index=False)

    result = task_func(csv_path, date_column)

    assert result.index.tolist() == [2022]
    assert result.values.tolist() == [3]

def test_task_func_invalid_csv_path():
    csv_path = os.path.join(OUTPUT_DIR, 'data.csv')
    date_column = 'date'

    with pytest.raises(FileNotFoundError):
        task_func(csv_path, date_column)