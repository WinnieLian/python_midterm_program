import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from additional_cleaning import additional_cleaning

non_zero_movies_df = pd.read_excel(
    "data/non_zero_revenue_or_budget_2000_2024.xlsx"
)

def correlation_heatmap(dataframe):
    """Generates correlation heatmap of budget, revenue, vote average, vote count, and runtime given dataframe as an input"""
    new_df = additional_cleaning(dataframe)
    numeric_only_df = new_df.select_dtypes(include=[np.number]).drop(["id", "total_budget", "release_year", "release_month", "release_quarter"], axis=1)
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_only_df.corr(), annot=True)
    plt.xticks(rotation=0, ha="center")
    return plt.show()

correlation_heatmap(non_zero_movies_df)

def regression_scatter_plot(dataframe, str):
    X = dataframe.select_dtypes(include=[np.number]).drop(['id','revenue'], axis=1)
    y = dataframe['revenue']

    plt.scatter(X[str], y, color = "blue")
    return plt.show()


def reg_OLS(dataframe):
    new_df = additional_cleaning(dataframe)
    X = new_df.select_dtypes(include=[np.number]).drop(["id","revenue", "release_month", "release_year", "budget", "release_quarter"], axis=1)
    X = sm.add_constant(X)
    y = new_df['revenue']
    model = sm.OLS(y, X)
    OLS_model = model.fit()
    predicted_y = OLS_model.predict(X)

    new_df['predicted_y'] = predicted_y
    plt.figure(figsize=(10, 6))
    
    sns.regplot(x=new_df['runtime'], 
                y=new_df['predicted_y'], 
                logistic=False,
                scatter = True,
                color='blue')

    return OLS_model.summary()



print(reg_OLS(non_zero_movies_df))

