import pandas as pd
import matplotlib.pyplot as plt
from additional_cleaning import additional_cleaning


non_zero_movies_df = pd.read_excel(
    "data/non_zero_revenue_or_budget_2000_2024.xlsx"
)

def retreive_avg_roi(dataframe):
    """Calculates average ROI group by genre and returns subset of data"""
    new_df = additional_cleaning(dataframe)
    average_values = new_df.groupby('genres').agg(
        avg_revenue=('revenue', 'mean'),
        avg_total_budget=('total_budget', 'mean')
        ).reset_index()
    
    average_values['avg_ROI'] = 100* (average_values['avg_revenue'] - average_values['avg_total_budget'])/(average_values['avg_total_budget'])
    
    return average_values


def return_on_investment_per_genre(dataframe):
    """Generates a horizontal bar graph of average ROI per genre"""
    x = retreive_avg_roi(dataframe) 
    plt.figure(figsize=(10,10))
    plt.barh(x['genres'], x['avg_ROI'])
    plt.xlabel('Return on Investment')
    return plt.show()


def return_on_investment_per_release_quarter(dataframe):
    "Generates a horizontal bar graph of average ROI per release quarter"
    new_df = additional_cleaning(dataframe)
    average_values = new_df.groupby('release_quarter').agg(
        avg_revenue=('revenue', 'mean'),
        avg_total_budget=('total_budget', 'mean')
        ).reset_index()
    
    average_values['avg_ROI'] = 100* (average_values['avg_revenue'] - average_values['avg_total_budget'])/(average_values['avg_total_budget'])
    
    plt.figure(figsize=(10,10))
    plt.barh(average_values['release_quarter'], average_values['avg_ROI'])
    plt.xlabel('Return on Investment')
    return plt.show()


def avg_vote_count_by_genre(dataframe):
    """Generates a horizontal bar graph of average vote count per genre"""
    average_vote_count = dataframe.groupby('genres')['vote_count'].mean()
    average_vote_count_df = average_vote_count.reset_index()
    average_vote_count_df.columns = ['genres', 'average_vote_count']

    plt.barh(average_vote_count_df['genres'], average_vote_count_df['average_vote_count'])
    plt.xlabel('Average Vote Count')
    return plt.show()

def avg_vote_count_by_release_quarter(dataframe):
    """Generates a horizontal bar graph of average vote count per release quarter"""
    new_df= additional_cleaning(dataframe)
    average_vote_count = new_df.groupby('release_quarter')['vote_count'].mean()
    average_vote_count_df = average_vote_count.reset_index()
    average_vote_count_df.columns = ['release_quarter', 'average_vote_count']

    plt.barh(average_vote_count_df['release_quarter'], average_vote_count_df['average_vote_count'])
    plt.xlabel('Average vote count')
    return plt.show()


def count_per_release_quarter(dataframe):
    """Generates a horizontal bar graph of total count of movies per release quarter"""
    new_df= additional_cleaning(dataframe)
    count = new_df.groupby('release_quarter').size()
    count_df = count.reset_index()
    count_df.columns = ['release_quarter', 'total_count']

    plt.barh(count_df['release_quarter'], count_df['total_count'])
    plt.xlabel('Number of Movies')
    return plt.show()


def avg_budget_per_genre(dataframe):
    """Generates a horizontal bar graph of average total budget per genre"""
    new_df = additional_cleaning(dataframe)
    average_budget = new_df.groupby('genres')['total_budget'].mean()
    average_budget_df = average_budget.reset_index()
    average_budget_df.columns = ['genres', 'average_total_budget']

    plt.barh(average_budget_df['genres'], average_budget_df['average_total_budget'])
    plt.xlabel('Average Total Budget')
    return plt.show()

def avg_budget_per_release_quarter(dataframe):
    """Generates a horizontal bar graph of average total budget per release quarter"""
    new_df = additional_cleaning(dataframe)
    average_budget = new_df.groupby('release_quarter')['total_budget'].mean()
    average_budget_df = average_budget.reset_index()
    average_budget_df.columns = ['release_quarter', 'average_total_budget']

    plt.barh(average_budget_df['release_quarter'], average_budget_df['average_total_budget'])
    plt.xlabel('Average Total Budget')
    return plt.show()



return_on_investment_per_genre(non_zero_movies_df)
return_on_investment_per_release_quarter(non_zero_movies_df)
avg_vote_count_by_genre(non_zero_movies_df)
avg_vote_count_by_release_quarter(non_zero_movies_df)
count_per_release_quarter(non_zero_movies_df)
avg_budget_per_genre(non_zero_movies_df)
avg_budget_per_release_quarter(non_zero_movies_df)


