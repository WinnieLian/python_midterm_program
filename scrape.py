
import os
import tmdbsimple as tmdb
import json
import csv

raw_data=[]
movie_total=[]
# Set your TMDB API key
api_key = 'fde77491a434af64d2bde10706e72d33'
tmdb.API_KEY = api_key

# Function to fetch movie details
def fetch_movie_details(movie_id):
    movie = tmdb.Movies(movie_id)
    data = movie.info()

    # Extract desired attributes
    
    attributes = {
        'title': data.get('title'),
        'production_countries': data.get('production_countries'),
        'revenue': data.get('revenue'),
        'id': data.get('id'),
        'genres': data.get('genres'),
        'vote_count': data.get('vote_count'),
        'original_language': data.get('original_language'),
        'imdb_id': data.get('imdb_id'),
        'release_date': data.get('release_date'),
        'popularity': data.get('popularity'),
        'budget': data.get('budget'),
        'vote_average': data.get('vote_average'),
        'runtime': data.get('runtime')
    }

    # Save the movie details to a JSON file
    raw_data.append(attributes)

# Function to fetch movie details within a date range
def fetch_movies_in_date_range(year):
    discover = tmdb.Discover()  # Instantiate Discover
    page = 1

    while True:
        # Discover movies based on release dates using keyword arguments
        response = discover.movie(
            year=year,
            page=page
        )

        if 'results' not in response:
            print("No more movies found.")
            break

        movies = response['results']
        print(page)

        for movie in movies:
            movie_id = movie.get('id')
            movie_total.append(movie_id)
            fetch_movie_details(movie_id)
        

        #if page >= response['total_pages']:
        if page>=500:
            break
        page += 1  # Go to the next page
       

# Example usage
fetch_movies_in_date_range(2024)
filename = "output.csv"

# 写入 CSV 文件
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    # 提取字典的键作为列名
    fieldnames = raw_data[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # 写入列名
    writer.writeheader()

    # 写入数据行
    writer.writerows(raw_data)

print(f"数据已成功写入 {filename} 文件。")