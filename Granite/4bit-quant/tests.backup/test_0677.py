import pandas as pd
import random
import pytest

def task_func(df):

    def determine_winner(row):
        if row['score1'] > row['score2']:
            return row['team1']
        elif row['score1'] < row['score2']:
            return row['team2']
        else:
            return random.choice([row['team1'], row['team2']])
    
    # Using pd.Series to explicitly create a new Series for the 'winner' column
    winner_series = pd.Series([determine_winner(row) for index, row in df.iterrows()], index=df.index)
    df['winner'] = winner_series
    return df

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'team1': ['Team A', 'Team B', 'Team C'],
        'team2': ['Team X', 'Team Y', 'Team Z'],
        'score1': [10, 5, 8],
        'score2': [8, 10, 5]
    })

    # Call the task_func function with the sample DataFrame
    result_df = task_func(df)

    # Define the expected output
    expected_df = pd.DataFrame({
        'team1': ['Team A', 'Team B', 'Team C'],
        'team2': ['Team X', 'Team Y', 'Team Z'],
        'score1': [10, 5, 8],
        'score2': [8, 10, 5],
        'winner': ['Team A', 'Team Y', 'Team C']
    })

    # Assert that the result_df matches the expected_df
    assert result_df.equals(expected_df)

if __name__ == '__main__':
    pytest.main()