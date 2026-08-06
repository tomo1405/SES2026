import numpy as np
import random
from difflib import SequenceMatcher
def task_func(s, min_length, max_length, letters):
    string_length = np.random.randint(min_length, max_length+1)
    generated_s = ''.join(random.choice(letters) for _ in range(string_length))

    # Check similarity
    similarity = SequenceMatcher(None, s, generated_s).ratio()
    is_similar = similarity >= 0.5

    return generated_s, is_similar