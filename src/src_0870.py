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