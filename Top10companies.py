import matplotlib.pyplot as plt
import pandas as pd

file_path_non_zero_revenue = '/Users/xuchengyang/Downloads/non_zero_revenue_2000_2024-2.xlsx'
non_zero_revenue_data = pd.read_excel(file_path_non_zero_revenue)


# Find release year
non_zero_revenue_data['release_date'] = pd.to_datetime(non_zero_revenue_data['release_date'], errors='coerce')
non_zero_revenue_data['release_year'] = non_zero_revenue_data['release_date'].dt.year

# Calculate the total revenue per year for all companies
company_year_revenue = non_zero_revenue_data.groupby(['production_companies', 'release_year'])['revenue'].sum().reset_index()
total_revenue_per_year = company_year_revenue.groupby('release_year')['revenue'].sum().reset_index()
total_revenue_per_year = total_revenue_per_year.rename(columns={'revenue': 'total_revenue'})

# Calculate each company's market share
company_year_revenue = company_year_revenue.merge(total_revenue_per_year, on='release_year')
company_year_revenue['market_share'] = company_year_revenue['revenue'] / company_year_revenue['total_revenue']

# Select top 10 companies with highest total revenue over the entire period
top_10_companies = company_year_revenue.groupby('production_companies')['revenue'].sum().nlargest(10).index
top_10_data = company_year_revenue[company_year_revenue['production_companies'].isin(top_10_companies)]
top_10_pivot = top_10_data.pivot(index='release_year', columns='production_companies', values='market_share').fillna(0)

# Sort companies by their total market share over the period to arrange legend in descending order
sorted_companies = top_10_pivot.sum().sort_values(ascending=False).index
top_10_pivot_sorted = top_10_pivot[sorted_companies]

# Complete the chart
plt.figure(figsize=(14, 8))
colors = plt.cm.Blues_r(range(100, 300, 20))
plt.stackplot(top_10_pivot_sorted.index, top_10_pivot_sorted.T, labels=top_10_pivot_sorted.columns, colors=colors, alpha=0.8)

plt.title('Market Share Over Time for Top 10 Production Companies (2000-2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Box Office Revenue (in Billions USD)', fontsize=14)
plt.xticks(ticks=range(2000, 2025, 1), rotation=45)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Production Companies', fontsize=8, frameon=False)
plt.tight_layout()
plt.show()
