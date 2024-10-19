import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load and process data from an Excel file."""
    data = pd.read_excel(file_path)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    data['release_year'] = data['release_date'].dt.year
    return data

def calculate_genre_revenue(data):
    """Calculate total revenue by genre and year."""
    genre_year_revenue = data.groupby(['genres', 'release_year'])['revenue'].sum().reset_index()

    genre_revenue_pivot = genre_year_revenue.pivot(index='release_year', columns='genres', values='revenue').fillna(0)
    return genre_revenue_pivot

def plot_genre_revenue_trends(data):
    """Plot revenue trends by movie genre over time."""
    plt.figure(figsize=(14, 8))
    for genre in data.columns:
        plt.plot(data.index, data[genre], label=genre, linewidth=1.5)

    plt.title('Revenue Trends by Movie Genre (2000-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Total Revenue (in Billions USD)', fontsize=14)
    plt.xticks(ticks=range(2000, 2025, 2), rotation=45)
    plt.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
    plt.tight_layout()

def save_plot(filename):
    """Save the plot to a specified directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'Images')
    os.makedirs(images_dir, exist_ok=True)

    save_path = os.path.join(images_dir, filename)
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()

def main():
    '''Run the code'''
    file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024.xlsx'

    non_zero_revenue_data = load_data(file_path_non_zero_revenue)

    genre_revenue_pivot = calculate_genre_revenue(non_zero_revenue_data)

    plot_genre_revenue_trends(genre_revenue_pivot)

    save_plot('Revenue_Trends_by_Movie_Genre_2000_2024.png')

if __name__ == '__main__':
    main()

