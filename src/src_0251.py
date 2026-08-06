import numpy as np
import itertools
import json
def task_func(data_list, json_file_name="mean_values.json"):
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean(column) for column in unzipped_data[1:]]

    results = {'Position {}'.format(i+1): mean_value for i, mean_value in enumerate(mean_values)}
    
    with open(json_file_name, 'w') as f:
        json.dump(results, f)

    return results