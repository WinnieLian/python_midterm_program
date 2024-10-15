import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = "all_data_2000_2024.xlsx"
data = pd.read_excel(file_path)

# Step 1: Check if 'release_date' column exists and is parsed correctly
if 'release_date' not in data.columns:
    raise ValueError("The 'release_date' column is missing from the dataset!")

# Step 2: Convert 'release_date' to datetime and create 'release_year' column
data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
data['release_year'] = data['release_date'].dt.year

# Step 3: Ensure 'budget' and 'revenue' columns are numeric
data['budget'] = pd.to_numeric(data['budget'], errors='coerce').fillna(0)
data['revenue'] = pd.to_numeric(data['revenue'], errors='coerce').fillna(0)

# Debug: Check if 'release_year' column was successfully created
print(data[['title', 'release_date', 'release_year']].head())

# Step 4: Get top 15 movies by budget
top_budget = data.nlargest(15, 'budget')

# Step 5: Get top 15 movies by revenue
top_revenue = data.nlargest(15, 'revenue')

# Plot 1: Top 15 Most Expensive Film Productions by Budget
plt.figure(figsize=(12, 8))
plt.barh(top_budget['title'] + ' (' + top_budget['release_year'].astype(str) + ')',
         top_budget['budget'] / 1e6, color='#1f77b4', edgecolor='black')
plt.title("Top 15 Most Expensive Film Productions (in Million USD)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Production Costs (Million USD)", fontsize=14)
plt.ylabel("Film (Year)", fontsize=14)
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)
plt.gca().invert_yaxis()  # Invert y-axis to have the largest at the top
plt.tight_layout()
plt.savefig("top_budget_films.png", dpi=300, bbox_inches='tight')
print("Plot saved as 'top_budget_films.png'")

# Plot 2: Top 15 Films by Box Office Revenue
plt.figure(figsize=(12, 8))
plt.barh(top_revenue['title'] + ' (' + top_revenue['release_year'].astype(str) + ')',
         top_revenue['revenue'] / 1e9, color='#2ca02c', edgecolor='black')
plt.title("Top 15 Films by Box Office Revenue (in Billion USD)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Box Office Revenue (Billion USD)", fontsize=14)
plt.ylabel("Film (Year)", fontsize=14)
plt.grid(axis='x', linestyle='--', linewidth=0.7, alpha=0.7)
plt.gca().invert_yaxis()  # Invert y-axis to have the largest at the top
plt.tight_layout()
plt.savefig("top_revenue_films.png", dpi=300, bbox_inches='tight')
print("Plot saved as 'top_revenue_films.png'")
