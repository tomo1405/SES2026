import pytest
from src_0890 import task_func

def test_task_func():
    data_dir = "path/to/data/dir"
    csv_file = "data.csv"
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_csv(os.path.join(data_dir, csv_file), index=False)

    result = task_func(data_dir, csv_file)

    assert result.equals(df)