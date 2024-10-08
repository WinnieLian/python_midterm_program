
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

from datetime import datetime

def fetch_movies_in_date_range():
    discover = tmdb.Discover()  # Instantiate Discover
    page = 1

    # 定义日期范围：2023年1月1日至2023年12月31日
    release_date_gte = "2020-01-01"
    release_date_lte = "2020-12-31"
    date_format = "%Y-%m-%d"  # 日期格式

    while True:
        # 使用 release_date.gte 和 release_date.lte 参数过滤电影发布日期
        response = discover.movie(
            release_date_gte=release_date_gte,
            release_date_lte=release_date_lte,
            page=page,
         
        )

        if 'results' not in response:
            print("No more movies found.")
            break

        movies = response['results']
        print(f"Processing page {page}")

        for movie in movies:
            movie_id = movie.get('id')
            release_date = movie.get('release_date')

            # 如果 release_date 为空，跳过这部电影
            if not release_date:
                continue

            # 将 release_date 转换为 datetime 对象
            movie_release_date = datetime.strptime(release_date, date_format)

            # 定义 2023 年的开始和结束日期
            start_date = datetime.strptime(release_date_gte, date_format)
            end_date = datetime.strptime(release_date_lte, date_format)

            # 检查 release_date 是否在 2023 年范围内
            if start_date <= movie_release_date <= end_date:
                movie_total.append(movie_id)
                fetch_movie_details(movie_id)
            else:
                print(f"Skipping Movie ID: {movie_id}, Release Date: {release_date}")

        # 限制为500页结果
        if page >= 500:
            break
        page += 1  # Go to the next pageç

# Example usage
fetch_movies_in_date_range()
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