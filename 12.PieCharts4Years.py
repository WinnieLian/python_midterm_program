import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    """Load and process data from an Excel file."""
    data = pd.read_excel(file_path)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    data['release_year'] = data['release_date'].dt.year
    return data

def calculate_genre_revenue(data):
    """Calculate total revenue by genre and year."""
    genre_year_revenue = data.groupby(['genres', 'release_year'])['revenue'].sum().reset_index()
    return genre_year_revenue

def prepare_pie_data(data, year, threshold=0.02):
    """Prepare data for the pie chart of a specific year, combining small segments."""
    year_data = data[data['release_year'] == year]

    if year_data.empty:
        print(f"No data available for year {year}.")
        return None

    year_data = year_data.sort_values(by='revenue', ascending=False)

    # Calculate percentages
    total_revenue = year_data['revenue'].sum()
    year_data['percentage'] = year_data['revenue'] / total_revenue

    # Combine small segments
    large_segments = year_data[year_data['percentage'] >= threshold]
    small_segments = year_data[year_data['percentage'] < threshold]

    if not small_segments.empty:
        other_row = pd.DataFrame({
            'genres': ['Other'],
            'revenue': [small_segments['revenue'].sum()],
            'percentage': [small_segments['percentage'].sum()]
        })
        large_segments = pd.concat([large_segments, other_row], ignore_index=True)

    return large_segments, total_revenue

def plot_genre_revenue_pie(data, total_revenue, year):
    """Plot a pie chart for genre revenue share of a given year."""
    labels = data['genres']
    sizes = data['revenue']
    percentages = [f"{size / total_revenue * 100:.1f}%" for size in sizes]

    # Create a gradient color map
    colors = plt.cm.viridis(np.linspace(0, 1, len(sizes)))

    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        sizes, labels=None, startangle=90, colors=colors, autopct='%1.1f%%',
        pctdistance=0.85, textprops=dict(color="black"), wedgeprops=dict(edgecolor='w')
    )

    # Adjust percentage labels further outside to reduce overlap
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
        autotext.set_position((autotext.get_position()[0] * 1.4, autotext.get_position()[1] * 1.4))

    # Add legend
    plt.legend(wedges, labels, title="Genres", loc="center left", bbox_to_anchor=(0.9, 0.5), fontsize=10)
    plt.title(f'Genre Revenue Share in {year}', pad=40)
    plt.axis('equal')

def save_plot(year, filename):
    """Save the plot to a specified directory."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'Images')
    os.makedirs(images_dir, exist_ok=True)

    save_path = os.path.join(images_dir, f'{filename}_{year}.png')
    plt.savefig(save_path, bbox_inches="tight")
    plt.close()

def main():
    '''Run the code'''
    file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024.xlsx'

    non_zero_revenue_data = load_data(file_path_non_zero_revenue)

    genre_year_revenue = calculate_genre_revenue(non_zero_revenue_data)

    years = [2000, 2012, 2020, 2024]

    for year in years:
        large_segments, total_revenue = prepare_pie_data(genre_year_revenue, year)
        
        if large_segments is not None:
            plot_genre_revenue_pie(large_segments, total_revenue, year)
            save_plot(year, 'Genre_Revenue_Share')

if __name__ == '__main__':
    main()
