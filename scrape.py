import requests
import csv

# Function to discover movies based on date range
def discover_movies(api_key, year, page=1):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&primary_release_year={year}&sort_by=popularity.desc&page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get movie details by movie ID
def get_movie_details(api_key, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        production_countries = data.get('production_countries', [])
        countries = [country['name'] for country in production_countries]

        production_companies = data.get('production_companies', [])
        company_names = ', '.join([company['name'] for company in production_companies])

        return {
            'id': data.get('id'),
            'title': data.get('title'),
            'budget': data.get('budget'),
            'revenue': data.get('revenue'),
            'vote_average': data.get('vote_average'),
            'vote_count': data.get('vote_count'),
            'release_date': data.get('release_date'),
            'runtime': data.get('runtime'),
            'genres': ', '.join([genre['name'] for genre in data.get('genres', [])]),
            'original_language': data.get('original_language'),
            'production_countries': countries,
            'production_companies': company_names
        }
    else:
        return None

# Function to save movies data to CSV (append mode after first batch)
def save_movies_to_csv(movies, year, append=False):
    filename = f"movies_{year}_filtered.csv"
    
    # Define the CSV file headers
    headers = ['id', 'title', 'budget', 'revenue', 'vote_average', 'vote_count', 'release_date', 'runtime', 'genres', 'original_language', 'production_countries', 'production_companies']
    
    # Determine write mode (write or append)
    write_mode = 'a' if append else 'w'
    
    # Write to CSV file
    with open(filename, mode=write_mode, newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write the header only if we're not appending (i.e., first batch)
        if not append:
            writer.writeheader()
        
        # Write movie rows
        for movie in movies:
            writer.writerow(movie)
    
    print(f"Data saved to {filename} (append mode: {append})")

# Main function to get all movie data for a specific year and filter by country
def get_all_movies_by_year_and_country(api_key, year, country):
    current_page = 1
    movies = []
    append = False  # Controls whether we append to the file or create it fresh
    
    # First API call to get total pages
    response = discover_movies(api_key, year, page=current_page)
    
    if response:
        total_pages = response['total_pages']
        print(f"Total Pages: {total_pages}")

        while current_page <= total_pages:
            # Get movies for the current page
            discovered_movies = response.get('results', [])
            
            for movie in discovered_movies:
                movie_id = movie.get('id')
                movie_details = get_movie_details(api_key, movie_id)
                
                if movie_details and country in movie_details['production_countries']:
                    movies.append(movie_details)
            
            # Every 10 pages or when reaching the last page, save the data to the same CSV file
            if current_page % 10 == 0 or current_page == total_pages:
                save_movies_to_csv(movies, year, append=append)
                movies = []  # Clear the list for the next batch
                append = True  # After the first write, we switch to append mode
            
            # Move to the next page
            current_page += 1
            if current_page <= total_pages:
                response = discover_movies(api_key, year, page=current_page)
    else:
        print("Failed to retrieve movie data")

# USE YOUR API_KEY
api_key = '945e56de4cbd0ded4d8a796c356a0f4f'
year = 2024  # Year
country = 'United States of America '  # Specify the country you want to filter by

# GET MOVIES ONLY FROM THE SPECIFIED COUNTRY FOR THE GIVEN YEAR
get_all_movies_by_year_and_country(api_key, year, country)
