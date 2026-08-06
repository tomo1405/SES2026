import pandas as pd
import random
import csv
def task_func(n, 
           categories=['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'],
           news_sites=['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'],
           likert_scale=['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'],
           file_path='news_survey_data.csv',
           random_seed=None):
    survey_data = []

    random.seed(random_seed)
    
    for _ in range(n):
        site = random.choice(news_sites)
        category = random.choice(categories)
        response = random.choice(likert_scale)
        value = likert_scale.index(response) + 1  # Assign a numerical value to the response
        survey_data.append({'Site': site, 'Category': category, 'Response': response, 'Value': value})
    
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['Site', 'Category', 'Response', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(survey_data)
        
    df = pd.read_csv(file_path)
    
    return df