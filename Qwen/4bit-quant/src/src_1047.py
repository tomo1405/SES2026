from datetime import datetime
import pandas as pd
from itertools import product
# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]
def task_func(date_str):
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    dates = pd.date_range(start_date, periods=10).tolist()

    # Creating a DataFrame from the product of EMPLOYEES and dates
    df = pd.DataFrame(list(product(EMPLOYEES, dates)), columns=["Employee", "Date"])

    return df