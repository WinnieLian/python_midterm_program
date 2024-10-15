import pandas as pd
import matplotlib.pyplot as plt

file_path = "all_data_2000_2024.xlsx"
data = pd.read_excel(file_path)

data['release_year'] = pd.to_datetime(data['release_date'], errors='coerce').dt.year
movies_per_year = data.groupby('release_year').size()

# Filter the years between 2000 to 2024
movies_per_year = movies_per_year.loc[2000:2024]

plt.figure(figsize=(12, 6))
plt.bar(movies_per_year.index, movies_per_year.values, color='lightblue', edgecolor='black')

x_labels = [str(year) if year != 2024 else "2024\n(YTD)" for year in movies_per_year.index]
plt.xticks(movies_per_year.index, x_labels, rotation=45)

plt.title("Number of Movies Released from 2000 to 2024", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Movies Released", fontsize=14)
plt.xticks(movies_per_year.index, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.savefig("movies_per_year.png")
print("Plot saved as 'movies_per_year.png'")


