python
import numpy as np
import matplotlib.pyplot as plt
from src_0338 import task_func

# Constants
COLORS = ['r', 'g', 'b']

# Test case 1
df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4]})
group_col = 'group'
value_col = 'value'
ax = task_func(df, group_col, value_col)
assert ax.get_xlabel() == group_col
assert ax.get_ylabel() == value_col
assert ax.get_title().get_text() == f'Bar chart of {value_col} by {group_col}'
assert ax.get_xticks() == (0, 1, 2, 3)
assert ax.get_xticklabels() == ('A', 'B')
assert ax.get_legend().get_texts()[0].get_text() == 'Group 1'
assert ax.get_legend().get_texts()[1].get_text() == 'Group 2'
assert ax.get_legend().get_texts()[2].get_text() == 'Group 3'
assert ax.get_legend().get_texts()[3].get_text() == 'Group 4'

# Test case 2
df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4], 'value2': [5, 6, 7, 8]})
group_col = 'group'
value_col = 'value'
ax = task_func(df, group_col, value_col)
assert ax.get_xlabel() == group_col
assert ax.get_ylabel() == value_col
assert ax.get_title().get_text() == f'Bar chart of {value_col} by {group_col}'
assert ax.get_xticks() == (0, 1, 2, 3)
assert ax.get_xticklabels() == ('A', 'B')
assert ax.get_legend().get_texts()[0].get_text() == 'Group 1'
assert ax.get_legend().get_texts()[1].get_text() == 'Group 2'
assert ax.get_legend().get_texts()[2].get_text() == 'Group 3'
assert ax.get_legend().get_texts()[3].get_text() == 'Group 4'

# Test case 3
df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4], 'value2': [5, 6, 7, 8]})
group_col = 'group'
value_col = 'value2'
ax = task_func(df, group_col, value_col)
assert ax.get_xlabel() == group_col
assert ax.get_ylabel() == value_col
assert ax.get_title().get_text() == f'Bar chart of {value_col} by {group_col}'
assert ax.get_xticks() == (0, 1, 2, 3)
assert ax.get_xticklabels() == ('A', 'B')
assert ax.get_legend().get_texts()[0].get_text() == 'Group 1'
assert ax.get_legend().get_texts()[1].get_text() == 'Group 2'
assert ax.get_legend().get_texts()[2].get_text() == 'Group 3'
assert ax.get_legend().get_texts()[3].get_text() == 'Group 4'

# Test case 4
df = pd.DataFrame({'group': ['A', 'A', 'B', 'B'], 'value': [1, 2, 3, 4], 'value2': [5, 6, 7, 8]})
group_col = 'group'
value_col = 'value3'
ax = task_func(df, group_col, value_col)
assert ax.get_xlabel() == group_col
assert ax.get_ylabel() == value_col
assert ax.get_title().get_text() == f'Bar chart of {value_col} by {group_col}'
assert ax.get_xticks() == (0, 1, 2, 3)
assert ax.get_xticklabels() == ('A', 'B')
assert ax.get_legend().get_texts()[0].get_text() == 'Group 1'
assert ax.get_legend().get_texts()[1].get_text() == 'Group 2'
assert ax.get_legend().get_texts()[2].get_text() == 'Group 3'
assert ax.get_legend().get_texts()[3].get_text() == 'Group 4'