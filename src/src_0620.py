from random import randint, seed
import pandas as pd
from sklearn.linear_model import LinearRegression
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTY_COST = 1000  # in dollars
def task_func(goals, penalties, rng_seed=None):
    if rng_seed is not None:
        seed(rng_seed)

    # Generate match results
    match_results = []
    for team in TEAMS:
        team_goals = randint(0, goals)
        team_penalties = randint(0, penalties)
        penalty_cost = PENALTY_COST * team_penalties
        match_results.append([team, team_goals, penalty_cost])

    # Create DataFrame
    results_df = pd.DataFrame(match_results, columns=['Team', 'Goals', 'Penalty Cost'])

    # Train Linear Regression Model
    X = results_df[['Goals']]
    y = results_df['Penalty Cost']
    model = LinearRegression().fit(X, y)

    return results_df, model