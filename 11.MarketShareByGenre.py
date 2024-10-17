import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024-2.xlsx'
non_zero_revenue_data = pd.read_excel(file_path_non_zero_revenue)

non_zero_revenue_data['release_date'] = pd.to_datetime(non_zero_revenue_data['release_date'], errors='coerce')
non_zero_revenue_data['release_year'] = non_zero_revenue_data['release_date'].dt.year

# Grouping the data by genre and release year
genre_year_revenue = non_zero_revenue_data.groupby(['genres', 'release_year'])['revenue'].sum().reset_index()

# Calculating the total revenue per year for all genres
total_revenue_per_year_genre = genre_year_revenue.groupby('release_year')['revenue'].sum().reset_index()
total_revenue_per_year_genre = total_revenue_per_year_genre.rename(columns={'revenue': 'total_revenue'})

# Merging the total revenue
genre_year_revenue = genre_year_revenue.merge(total_revenue_per_year_genre, on='release_year')
genre_year_revenue['market_share'] = genre_year_revenue['revenue'] / genre_year_revenue['total_revenue']

# Selecting the top 10 genres by total revenue over the entire period
top_genres = genre_year_revenue.groupby('genres')['revenue'].sum().nlargest(10).index
top_genre_data = genre_year_revenue[genre_year_revenue['genres'].isin(top_genres)]

top_genre_pivot = top_genre_data.pivot(index='release_year', columns='genres', values='market_share').fillna(0)

other_genre_data = genre_year_revenue[~genre_year_revenue['genres'].isin(top_genres)]
other_genre_yearly = other_genre_data.groupby('release_year')['market_share'].sum()
top_genre_pivot['Other'] = other_genre_yearly

# Define the color
cmap = mcolors.LinearSegmentedColormap.from_list('teal_green_yellow', ['#4682B4', '#3CB371', '#FFFF66', '#FFE4B5'])

# Plotting
plt.figure(figsize=(14, 8))
top_genre_pivot.plot(kind='bar', stacked=True, figsize=(14, 8), colormap=cmap, width=0.8, alpha=0.85)

plt.title('Box Office Revenue Share by Genre (2000-2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Box Office Revenue (in Billions USD)', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Genres')
plt.tight_layout()
plt.show()
