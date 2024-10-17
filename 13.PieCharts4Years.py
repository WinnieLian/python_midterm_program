import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

file_path_non_zero_revenue = 'data/non_zero_revenue_2000_2024-2.xlsx'
non_zero_revenue_data = pd.read_excel(file_path_non_zero_revenue)

# Extract release year from release_date
non_zero_revenue_data['release_date'] = pd.to_datetime(non_zero_revenue_data['release_date'], errors='coerce')
non_zero_revenue_data['release_year'] = non_zero_revenue_data['release_date'].dt.year

# Grouping and summing up
genre_year_revenue = non_zero_revenue_data.groupby(['genres', 'release_year'])['revenue'].sum().reset_index()

years = [2000, 2012, 2020, 2024]

# Generate pie charts
for year in years:
    year_data = genre_year_revenue[genre_year_revenue['release_year'] == year]
    
    if year_data.empty:
        print(f"No data available for year {year}.")
        continue
    
    year_data = year_data.sort_values(by='revenue', ascending=False)
    
    # Combine small segments
    threshold = 0.02
    total_revenue = year_data['revenue'].sum()
    year_data['percentage'] = year_data['revenue'] / total_revenue
    large_segments = year_data[year_data['percentage'] >= threshold]
    small_segments = year_data[year_data['percentage'] < threshold]
    
    if not small_segments.empty:
        other_row = pd.DataFrame({'genres': ['Other'], 'revenue': [small_segments['revenue'].sum()], 'percentage': [small_segments['percentage'].sum()]})
        large_segments = pd.concat([large_segments, other_row], ignore_index=True)
    
    # Pie chart values and labels
    labels = large_segments['genres']
    sizes = large_segments['revenue']
    percentages = [f"{size / total_revenue * 100:.1f}%" for size in sizes]
    
     # Create a gradient color map
    colors = plt.cm.viridis(np.linspace(0, 1, len(sizes)))

    # Plot
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        sizes, labels=None, startangle=90, colors=colors, autopct='%1.1f%%',
        pctdistance=0.85, textprops=dict(color="black"), wedgeprops=dict(edgecolor='w')
    )
    
    # Adjust percentage labels further outside the pie chart to reduce overlap
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
        autotext.set_position((autotext.get_position()[0] * 1.4, autotext.get_position()[1] * 1.4))
    
    # Add legend with genres in the order of the pie
    plt.legend(wedges, labels, title="Genres", loc="center left", bbox_to_anchor=(0.9, 0.5), fontsize=10)
    
    # Adjust title position further up
    plt.title(f'Genre Revenue Share in {year}', pad=40)  # Increase padding for title position
    plt.axis('equal')
    plt.show()
