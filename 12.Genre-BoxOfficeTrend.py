import pandas as pd
import matplotlib.pyplot as plt

file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024-2.xlsx'
non_zero_revenue_data = pd.read_excel(file_path_non_zero_revenue)

non_zero_revenue_data['release_date'] = pd.to_datetime(non_zero_revenue_data['release_date'], errors='coerce')
non_zero_revenue_data['release_year'] = non_zero_revenue_data['release_date'].dt.year

# Grouping the data and summing up the revenue per genre per year
genre_year_revenue = non_zero_revenue_data.groupby(['genres', 'release_year'])['revenue'].sum().reset_index()

# Pivoting the data
genre_revenue_pivot = genre_year_revenue.pivot(index='release_year', columns='genres', values='revenue').fillna(0)

# Plotting
plt.figure(figsize=(14, 8))
for genre in genre_revenue_pivot.columns:
    plt.plot(genre_revenue_pivot.index, genre_revenue_pivot[genre], label=genre, linewidth=1.5)

plt.title('Revenue Trends by Movie Genre (2000-2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total Revenue (in Billions USD)', fontsize=14)
plt.xticks(ticks=range(2000, 2025, 2), rotation=45)
plt.legend(title='Genres', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.tight_layout()
plt.show()
