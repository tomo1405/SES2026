python
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
    # Test case 1: Test with a sample dataframe
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [3, 2, 1]})
    expected_df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, 3], 'score2': [3, 2, 1], 'winner': ['A', 'E', 'C']})
    assert task_func(df).equals(expected_df)

    # Test case 2: Test with an empty dataframe
    df = pd.DataFrame({'team1': [], 'team2': [], 'score1': [], 'score2': []})
    expected_df = pd.DataFrame({'team1': [], 'team2': [], 'score1': [], 'score2': [], 'winner': []})
    assert task_func(df).equals(expected_df)

    # Test case 3: Test with a dataframe with NaN values
    df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, None], 'score2': [3, 2, 1]})
    expected_df = pd.DataFrame({'team1': ['A', 'B', 'C'], 'team2': ['D', 'E', 'F'], 'score1': [1, 2, None], 'score2': [3, 2, 1], 'winner': ['A', 'E', 'C']})
    assert task_func(df).equals(expected_df)

    # Test case 4: Test with a dataframe with all NaN values
    df = pd.DataFrame({'team1': [None, None, None], 'team2': [None, None, None], 'score1': [None, None, None], 'score2': [None, None, None]})
    expected_df = pd.DataFrame({'team1': [None, None, None], 'team2': [None, None, None], 'score1': [None, None, None], 'score2': [None, None, None], 'winner': [None, None, None]})
    assert task_func(df).equals(expected_df)