import re
from collections import Counter
def task_func(input_str):
    cleaned_str = re.sub('[^A-Za-z0-9]+', '', input_str).lower()
    freq_dict = Counter(cleaned_str)
    return freq_dict