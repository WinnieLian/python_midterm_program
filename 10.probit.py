
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from additional_cleaning import additional_cleaning


non_zero_movies_df = pd.read_excel(
    "C:/Users/Admin/Desktop/Python-Class/python_midterm_program/data/non_zero_revenue_or_budget_2000_2024.xlsx"
)
non_zero_bo_movies_df = pd.read_excel(
    "C:/Users/Admin/Desktop/Python-Class/python_midterm_program/data/non_zero_revenue_2000_2024.xlsx"
)


def get_probit_model(dataframe, str): 
    new_df = additional_cleaning(dataframe)
    profit = []
    for i in range(len(new_df['revenue'])):
        if new_df['revenue'][i] >= new_df['total_budget'][i]:
            profit.append({'profitability':1})
        else:
            profit.append({'profitability':0})
    
    profit_df = pd.DataFrame(profit)
    
    df_with_profit = pd.merge(new_df, profit_df, left_index=True, right_index=True)

    Y = df_with_profit['profitability']
    X = df_with_profit.select_dtypes(include=[np.number]).drop(["id","revenue", "release_month", "release_year","budget", "profitability", "total_budget","release_quarter"],  axis=1)
    model = sm.Probit(Y, X)
    probit_model = model.fit()
    predicted_probabilities = probit_model.predict(X)

    df_with_profit['predicted_probabilities'] = predicted_probabilities
    plt.figure(figsize=(10, 6))
    
    sns.regplot(x=df_with_profit[str], 
                y=df_with_profit['predicted_probabilities'], 
                logistic=True,
                scatter = True,
                color='blue')
    plt.ylabel("Probability of Profit")
    return plt.show()

get_probit_model(non_zero_movies_df, 'vote_average')
get_probit_model(non_zero_movies_df, 'vote_count')
get_probit_model(non_zero_movies_df, 'runtime')


