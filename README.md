

In this project, we gathered extensive movie data using The Movie Database (TMDb) API'https://www.themoviedb.org/?language=en-US', focusing on films released between 2000 and 2024 from various countries. By utilizing two key API endpoints—the Discover Movies and Movie Details endpoints—we were able to capture a comprehensive dataset on films from specific years and countries, including Budget (in dollars), Revenue (in dollars), Runtime (in minutes), Genres ( a list of genres for the movie), Production countries (a list of countries where the movie was produced), and Production companies (a list of companies involved in the movie's production)


Basic Movie Information
Initially, we used the Discover Movies endpoint to filter movies based on their release year and country of origin and employed random sampling to capture a diverse set of movies. This approach allowed us to efficiently gather data while avoiding potential biases associated with focusing solely on the most popular films. 

Detailed Movie Information
After identifying movies via the Discover endpoint, we retrieved additional data using the Movie Details endpoint. For each movie, we collected detailed information such as budget (in dollars), revenue (in dollars), runtime (in minutes), genres (a list of associated genres), production countries (the countries involved in production), and production companies (the companies involved in the film's creation). This allowed us to build a richer dataset for deeper analysis.

Data Storage:
The collected movie data was stored in CSV files for easy access and future analysis. Using csv.DictWriter, we initially created the file with headers to maintain a consistent structure across the dataset. As we processed batches of movies, we appended the data to the CSV file in order to avoid overwriting previous entries. This method ensured efficient storage and management of large datasets, particularly when dealing with multiple years' worth of data.

Changing the release year parameter
To cover the full scope of our project, we retrieved movie data from the TMDb API for 24 years, spanning from 2000 to 2024. By changing the release year parameter in the API calls, we were able to systematically collect data for each year. This comprehensive dataset reflects two decades of film industry trends, including financial data such as budget and revenue, as well as insights into production practices across different countries and companies.























