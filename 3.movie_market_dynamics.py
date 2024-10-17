import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel data
def load_data(file_path):
    return pd.read_excel(file_path)

# Prepare data for movies per year
def prepare_movies_per_year(data):
    data['release_year'] = pd.to_datetime(data['release_date'], errors='coerce').dt.year
    movies_per_year = data.groupby('release_year').size()
    return movies_per_year.loc[2000:2024]  # Filter years between 2000 and 2024

# Plot movies released per year
def plot_movies_per_year(movies_per_year):
    plt.figure(figsize=(12, 6))
    plt.bar(movies_per_year.index, movies_per_year.values, color='lightblue', edgecolor='black')

    x_labels = [str(year) if year != 2024 else "2024\n(YTD)" for year in movies_per_year.index]
    plt.xticks(movies_per_year.index, x_labels, rotation=45)

    plt.title("Number of Movies Released from 2000 to 2024", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Number of Movies Released", fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("movies_per_year.png")
    print("Plot saved as 'movies_per_year.png'")

# Prepare data for revenue per year
def prepare_revenue_per_year(data):
    data['release_year'] = pd.to_datetime(data['release_date'], errors='coerce').dt.year
    data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').fillna(0)  # Handle non-numeric revenue
    revenue_per_year = data.groupby('release_year')['revenue'].sum()
    return revenue_per_year.loc[2000:2024]  # Filter years between 2000 and 2024

# Plot box office revenue per year
def plot_revenue_per_year(revenue_per_year):
    plt.figure(figsize=(12, 6))
    plt.bar(revenue_per_year.index, revenue_per_year.values / 1e9,  # Convert to billions
            color='lightgreen', edgecolor='black')

    x_labels = [str(year) if year != 2024 else "2024\n(YTD)" for year in revenue_per_year.index]
    plt.xticks(revenue_per_year.index, x_labels, rotation=45, fontsize=12)

    plt.title("Total Box Office Revenue from 2000 to 2024", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Box Office Revenue (in Billions USD)", fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("box_office_revenue.png")
    print("Plot saved as 'box_office_revenue.png'")

# Main function to orchestrate the tasks
def main():
    file_path = "data/all_data_2000_2024.xlsx"
    data = load_data(file_path)

    # Prepare and plot movies per year
    movies_per_year = prepare_movies_per_year(data)
    plot_movies_per_year(movies_per_year)

    # Prepare and plot revenue per year
    revenue_per_year = prepare_revenue_per_year(data)
    plot_revenue_per_year(revenue_per_year)

# Execute the main function
if __name__ == "__main__":
    main()
