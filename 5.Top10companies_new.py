import os
import matplotlib.pyplot as plt
import pandas as pd

def load_data(file_path):
    """Load and process data from an Excel file."""
    data = pd.read_excel(file_path)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    data['release_year'] = data['release_date'].dt.year
    return data

def calculate_market_share(data):
    """Calculate the market share for production companies over years."""
    company_year_revenue = data.groupby(['production_companies', 'release_year'])['revenue'].sum().reset_index()

    total_revenue_per_year = company_year_revenue.groupby('release_year')['revenue'].sum().reset_index()
    total_revenue_per_year = total_revenue_per_year.rename(columns={'revenue': 'total_revenue'})

    company_year_revenue = company_year_revenue.merge(total_revenue_per_year, on='release_year')
    company_year_revenue['market_share'] = company_year_revenue['revenue'] / company_year_revenue['total_revenue']

    return company_year_revenue

def filter_top_companies(data, top_n=10):
    """Filter the top N companies based on total revenue."""
    top_companies = data.groupby('production_companies')['revenue'].sum().nlargest(top_n).index
    top_data = data[data['production_companies'].isin(top_companies)]

    top_pivot = top_data.pivot(index='release_year', columns='production_companies', values='market_share').fillna(0)

    sorted_companies = top_pivot.sum().sort_values(ascending=False).index
    top_pivot_sorted = top_pivot[sorted_companies]

    return top_pivot_sorted

def plot_market_share_over_time(data):
    """Plot the market share over time for the top production companies."""
    plt.figure(figsize=(14, 8))
    colors = plt.cm.tab20(range(10))

    plt.stackplot(data.index, data.T, labels=data.columns, colors=colors, alpha=0.8)

    plt.title('Market Share Over Time for Top 10 Production Companies (2000-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Market Share (%)', fontsize=14)
    plt.xticks(ticks=range(2000, 2025, 1), rotation=45)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Production Companies', fontsize=8, frameon=False)
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

    company_year_revenue = calculate_market_share(non_zero_revenue_data)

    top_10_pivot_sorted = filter_top_companies(company_year_revenue)

    plot_market_share_over_time(top_10_pivot_sorted)

    save_plot('Market_Share_Top_10_Production_Companies_2000_2024.png')

if __name__ == '__main__':
    main()
