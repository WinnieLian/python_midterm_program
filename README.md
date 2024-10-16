# Python_Midterm_Project 

For this project, we collected movie data from The Movie Database (TMDb) API, focusing on films released in a specific year and country. The data collection involved two API endpoints: the Discover Movies endpoint, which was used to fetch movies based on release year and country of origin, and the Movie Details endpoint, which provided detailed information for each movie, including Budget (in dollars), Revenue (in dollars), Runtime (in minutes), Genres ( a list of genres for the movie), Production countries (a list of countries where the movie was produced), and Production companies (a list of companies involved in the movie's production).

The collected data was stored in a CSV file using csv.DictWriter. Initially, the file was created with headers to establish a consistent structure. As more movie batches were processed, data was appended to avoid overwriting, ensuring efficient storage and management of large datasets. 

