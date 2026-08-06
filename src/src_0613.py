from random import choice
import numpy as np
import pandas as pd
# Constants
TEAMS = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
PENALTIES_COSTS = [100, 200, 300, 400, 500]
def task_func(goals, penalties, teams=TEAMS, penalties_costs=PENALTIES_COSTS):
    report_data = []
    for team in teams:
        team_goals = goals.get(team, 0)
        team_penalties = penalties.get(team, 0)
        penalties_cost = team_penalties * choice(penalties_costs)
        performance_score = np.max([0, team_goals - team_penalties])
        report_data.append({
            'Team': team,
            'Goals': team_goals,
            'Penalties': team_penalties,
            'Penalties Cost': penalties_cost,
            'Performance Score': performance_score
        })

    report_df = pd.DataFrame(report_data)
    return report_df