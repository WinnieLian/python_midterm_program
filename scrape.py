import requests

def discover_movies(api_key, year,country,page):
    '''Function to discover movies based on date range'''
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&primary_release_year={year}&with_origin_country={country}&sort_by=popularity.desc&page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_movie_details(api_key, movie_id):
    '''Function to get movie details by movie ID'''
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

def get_all_movies_by_year_and_country(api_key, year, country):
    '''Main function to get all movie data for a specific year and filter by country'''
    current_page = 1
    movies = []
    append = False 
    
  
    response = discover_movies(api_key, year, country, page=current_page)
    
    if response:
        total_pages = response['total_pages']
        print(f"Total Pages: {total_pages}")
        while current_page <= total_pages:
           
            discovered_movies = response.get('results', [])
            
            for movie in discovered_movies:
                movie_id = movie.get('id')
                movie_details = get_movie_details(api_key, movie_id)
                movies.append(movie_details)
            
          
            current_page += 1
            if current_page <= total_pages:
                response = discover_movies(api_key, year, country, page=current_page)
    else:
        print("Failed to retrieve movie data")

'''GET MOVIES ONLY FROM THE SPECIFIED COUNTRY FOR THE GIVEN YEAR'''
api_key = '945e56de4cbd0ded4d8a796c356a0f4f'
year = 2010 
country = 'US' 
 
get_all_movies_by_year_and_country(api_key, year, country)