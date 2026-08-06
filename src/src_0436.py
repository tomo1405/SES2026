import pandas as pd
from random import randint
def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "David"]
    JOBS = ["Engineer", "Manager", "Analyst", "Developer", "Tester"]

    if name not in EMPLOYEES:
        raise ValueError(f"Invalid employee name. Must be one of {EMPLOYEES}")

    job = JOBS[randint(0, len(JOBS) - 1)]
    data_df = pd.DataFrame(
        [[name, age, code, salary, bio, job]],
        columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"],
    )
    return data_df