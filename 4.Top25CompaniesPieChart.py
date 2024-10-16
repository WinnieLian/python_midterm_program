import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024-2.xlsx'
non_zero_revenue_data = pd.read_excel(file_path_non_zero_revenue)

non_zero_revenue_data['release_date'] = pd.to_datetime(non_zero_revenue_data['release_date'], errors='coerce')
non_zero_revenue_data['release_year'] = non_zero_revenue_data['release_date'].dt.year

# Filter data and compute average revenue
filtered_data = non_zero_revenue_data[non_zero_revenue_data['release_year'].between(2020, 2024)]
average_revenue = filtered_data.groupby('production_companies')['revenue'].mean()

# Calculate revenue percentage
top_25_companies = average_revenue.nlargest(25)
total_revenue = top_25_companies.sum()

revenue_share = top_25_companies / total_revenue
large_segments = revenue_share[revenue_share >= 0.02]
small_segments = revenue_share[revenue_share < 0.02]

if not small_segments.empty:
    other_row = pd.Series(small_segments.sum(), index=['Other'])
    large_segments = pd.concat([large_segments, other_row])

#Plotting
labels = large_segments.index
sizes = large_segments.values

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

plt.savefig('/Users/xuchengyang/Downloads/Top_25_Companies_Average_Revenue_Share_2020_2024_final.png', bbox_inches="tight")
plt.close()
