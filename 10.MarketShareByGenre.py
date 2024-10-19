import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def load_data(file_path):
    """Load and process data from an Excel file."""
    data = pd.read_excel(file_path)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    data['release_year'] = data['release_date'].dt.year
    return data

def calculate_genre_market_share(data):
    """Calculate the market share for each genre over the years."""
    genre_year_revenue = data.groupby(['genres', 'release_year'])['revenue'].sum().reset_index()

    total_revenue_per_year = genre_year_revenue.groupby('release_year')['revenue'].sum().reset_index()
    total_revenue_per_year = total_revenue_per_year.rename(columns={'revenue': 'total_revenue'})

    genre_year_revenue = genre_year_revenue.merge(total_revenue_per_year, on='release_year')
    genre_year_revenue['market_share'] = genre_year_revenue['revenue'] / genre_year_revenue['total_revenue']

    return genre_year_revenue

def filter_top_genres(data, top_n=10):
    """Filter the top N genres based on total revenue and calculate 'Other' category."""
    top_genres = data.groupby('genres')['revenue'].sum().nlargest(top_n).index
    top_genre_data = data[data['genres'].isin(top_genres)]

    top_genre_pivot = top_genre_data.pivot(index='release_year', columns='genres', values='market_share').fillna(0)

    other_genre_data = data[~data['genres'].isin(top_genres)]
    other_genre_yearly = other_genre_data.groupby('release_year')['market_share'].sum()
    top_genre_pivot['Other'] = other_genre_yearly

    return top_genre_pivot

def plot_genre_market_share(data):
    """Plot the box office revenue share by genre over time."""
    cmap = mcolors.LinearSegmentedColormap.from_list('teal_green_yellow', ['#4682B4', '#3CB371', '#FFFF66', '#FFE4B5'])

    plt.figure(figsize=(14, 8))
    data.plot(kind='bar', stacked=True, figsize=(14, 8), colormap=cmap, width=0.8, alpha=0.85)

    plt.title('Box Office Revenue Share by Genre (2000-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Box Office Revenue (in Billions USD)', fontsize=14)
    plt.xticks(rotation=45)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Genres')
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
    ''''Run the code'''

    file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024.xlsx'

    non_zero_revenue_data = load_data(file_path_non_zero_revenue)

    genre_year_revenue = calculate_genre_market_share(non_zero_revenue_data)

    top_genre_pivot = filter_top_genres(genre_year_revenue)

    plot_genre_market_share(top_genre_pivot)

    save_plot('Box_Office_Revenue_Share_by_Genre_2000_2024.png')

# Run the main function
if __name__ == '__main__':
    main()
