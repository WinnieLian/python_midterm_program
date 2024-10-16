# Python_Midterm_Project 

For this project, we collected movie data from The Movie Database (TMDb) API, focusing on films released in a specific year and country. The data collection involved two API endpoints: the Discover Movies endpoint, which was used to fetch movies based on release year and country of origin, and the Movie Details endpoint, which provided detailed information for each movie, including Budget (in dollars), Revenue (in dollars), Runtime (in minutes), Genres ( a list of genres for the movie), Production countries (a list of countries where the movie was produced), and Production companies (a list of companies involved in the movie's production).

The collected data was stored in a CSV file using csv.DictWriter. Initially, the file was created with headers to establish a consistent structure. As more movie batches were processed, data was appended to avoid overwriting, ensuring efficient storage and management of large datasets. 


**Task 1:  Analysis of historical dynamics of US Movie market in 2000 - 2024**

In the first stage of our analysis, it was crucial to look at overall dynamics of number of films of the 24. For that we calculated number of films per each year of study, and the results can be seen below. It can be seen that the movie market has experienced steady growth over the whole period of study, with number of short-term decreases: a decrease in 2010, consequence of mortgage crisis of 2008-09 years and a slight decrease in 2020, caused by the problems with film production in COVID-19 pandemic. Additionally, it is necessary to mention that 2024 YTD data suggests a decrease in releases so far, but it’s too early to draw firm conclusions about the year’s overall trend.



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/Images-for-README/Images/movies_per_year.png?raw=true)

Then, we analyzed the total box office revenue of US, treating it as a proxy for overall movie market. Thus, in 2023 year the overall US movie market market was equal to around $12 bln. To dig deeper, we can clearly see a steady growth in box office revenue from 2000 to 2019 years coupled with a number of negligible decreases. However, the pandemic-induced disruption in 2020 caused the most significant revenue decline in modern history. The partial recovery from 2021 to 2023 suggests the industry is slowly regaining strength, though full recovery to pre-pandemic levels is still uncertain. 2024 YTD revenue indicates a slow start, but final figures may change depending on blockbuster releases later in the year.  



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/Images-for-README/Images/box_office_revenue.png?raw=true)















