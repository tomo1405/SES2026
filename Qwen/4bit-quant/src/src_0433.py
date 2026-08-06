import seaborn as sns
from scipy.stats import chi2_contingency
def task_func(df1, df2, column1="feature1", column2="feature2"):
    df = pd.merge(df1, df2, on="id")
    contingency_table = pd.crosstab(df[column1], df[column2])
    heatmap = sns.heatmap(contingency_table)
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return p, heatmap