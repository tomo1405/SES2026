import pandas as pd
from itertools import cycle
from random import randint, seed

def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):

    if len(students) == 0:
        raise ValueError("The students list should contain at least one student.")

    seed(rng_seed)

    student_cycle = cycle(students)
    grade_data = []

    for _ in range(n_grades):
        student = next(student_cycle)
        grade = randint(min(grade_range), max(grade_range))
        grade_data.append([student, grade])

    grade_df = pd.DataFrame(grade_data, columns=['Student', 'Grade'])

    return grade_df

import pytest

def test_task_func():
    # Test case 1: Test with no students
    with pytest.raises(ValueError):
        task_func(n_grades=0, students=[])

    # Test case 2: Test with one student
    grade_df = task_func(n_grades=1, students=['Alice'])
    assert grade_df.shape == (1, 2)
    assert grade_df['Student'].iloc[0] == 'Alice'
    assert grade_df['Grade'].iloc[0] >= 1 and grade_df['Grade'].iloc[0] <= 10

    # Test case 3: Test with multiple students and grades
    grade_df = task_func(n_grades=5, students=['Alice', 'Bob', 'Charlie'], grade_range=range(1, 6))
    assert grade_df.shape == (5, 2)
    assert set(grade_df['Student']) == set(['Alice', 'Bob', 'Charlie'])
    assert all(grade_df['Grade'] >= 1) and all(grade_df['Grade'] <= 5)

if __name__ == '__main__':
    test_task_func()