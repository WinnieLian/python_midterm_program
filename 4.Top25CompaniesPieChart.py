import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load data from an Excel file."""
    data = pd.read_excel(file_path)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    data['release_year'] = data['release_date'].dt.year
    return data

def filter_and_average_revenue(data, start_year, end_year):
    """Filter data by year range and compute average revenue for production companies."""
    filtered_data = data[data['release_year'].between(start_year, end_year)]
    average_revenue = filtered_data.groupby('production_companies')['revenue'].mean()
    return average_revenue

def calculate_revenue_share(average_revenue, top_n=25):
    """Calculate revenue share for the top N production companies."""
    top_companies = average_revenue.nlargest(top_n)
    total_revenue = top_companies.sum()
    
    revenue_share = top_companies / total_revenue
    large_segments = revenue_share[revenue_share >= 0.02]
    small_segments = revenue_share[revenue_share < 0.02]

    if not small_segments.empty:
        other_row = pd.Series(small_segments.sum(), index=['Other'])
        large_segments = pd.concat([large_segments, other_row])

    return large_segments

def plot_revenue_share(segments):
    """Plot the revenue share of production companies."""
    labels = segments.index
    sizes = segments.values

    plt.figure(figsize=(10, 10))
    colors = plt.cm.tab20c.colors + plt.cm.Paired.colors[:(len(labels) - len(plt.cm.tab20c.colors))]
    wedges, texts, autotexts = plt.pie(
        sizes, labels=None, startangle=90, colors=colors, autopct='%1.1f%%',
        pctdistance=0.85, textprops=dict(color="black")
    )

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
        autotext.set_position((autotext.get_position()[0] * 1.2, autotext.get_position()[1] * 1.2))

    plt.legend(wedges, labels, title="Companies", loc="center left", bbox_to_anchor=(1.2, 0.5), fontsize=10)
    plt.title('Top 25 Companies Average Revenue Share (2020-2024)', pad=40)
    plt.axis('equal')

def save_plot(filename):
    """Save the plot to a specified directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'Images')
    os.makedirs(images_dir, exist_ok=True)

    save_path = os.path.join(images_dir, filename)
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()

def main():
    '''Run code'''
    file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024.xlsx'

    non_zero_revenue_data = load_data(file_path_non_zero_revenue)

    average_revenue = filter_and_average_revenue(non_zero_revenue_data, 2020, 2024)

    large_segments = calculate_revenue_share(average_revenue)

    plot_revenue_share(large_segments)

    save_plot('Top_25_Companies_Average_Revenue_Share_2020_2024_final.png')

if __name__ == '__main__':
    main()