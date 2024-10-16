import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import math
import statsmodels.api as sm
from additional_cleaning import additional_cleaning

non_zero_movies_df = pd.read_excel(
    "C:/Users/Admin/Desktop/Python-Class/python_midterm_program/data/non_zero_revenue_or_budget_2000_2024.xlsx"
)
non_zero_bo_movies_df = pd.read_excel(
    "C:/Users/Admin/Desktop/Python-Class/python_midterm_program/data/non_zero_revenue_2000_2024.xlsx"
)

def correlation_heatmap(dataframe):
    """Generates correlation heatmap of budget, revenue, vote average, vote count, and runtime given dataframe as an input"""
    new_df = additional_cleaning(dataframe)
    numeric_only_df = new_df.select_dtypes(include=[np.number]).drop(["id", "total_budget", "release_year", "release_month", "release_quarter"], axis=1)
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_only_df.corr(), annot=True)
    plt.xticks(rotation=0, ha="center")
    return plt.show()


def regression_scatter_plot(dataframe, str):
    X = dataframe.select_dtypes(include=[np.number]).drop(["id","revenue"], axis=1)
    y = dataframe['revenue']

    plt.scatter(X[str], y, color = "blue")
    return plt.show()



def regression_analysis(dataframe):
    new_df = additional_cleaning(dataframe)
    X = new_df.select_dtypes(include=[np.number]).drop(["id","revenue", "release_month", "release_year"], axis=1)
    y = np.log(new_df['revenue'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    roi_prediction = linear_model.predict(X_test)

    rmse = float(math.sqrt(np.mean( (y_test - roi_prediction)**2 )))
    r2 = r2_score(y_test, roi_prediction)

    return ["Root Mean squared error is {}".format(rmse), "R_squared is {}".format(r2)]



def reg_OLS(dataframe):
    new_df = additional_cleaning(dataframe)
    X = new_df.select_dtypes(include=[np.number]).drop(["id","revenue", "release_month", "release_year", "budget", "vote_average", "release_quarter"], axis=1)
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

