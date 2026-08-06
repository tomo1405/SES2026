from collections import Counter
import itertools
def task_func(letters: list, repetitions: int) -> dict:
    # Create a flattened list by repeating the original list
    flattened_list = list(itertools.chain(*[letters for _ in range(repetitions)]))
    
    # Count the occurrences of each letter in the flattened list
    counts = dict(Counter(flattened_list))
    
    return counts