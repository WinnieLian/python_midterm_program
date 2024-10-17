# Python_Midterm_Project 

**Group Members**:  Maksim Korenev, Chengyang Xu, Huiwen Lian, Ningtao Xu, Vignesh Avadhanam

**Project Description**: Analysis of US movie market 2000-2024 

For this project, we collected movie data from The Movie Database (TMDb) API, focusing on films released in a specific year and country. The data collection involved two API endpoints: the Discover Movies endpoint, which was used to fetch movies based on release year and country of origin, and the Movie Details endpoint, which provided detailed information for each movie, including Budget (in dollars), Revenue (in dollars), Runtime (in minutes), Genres ( a list of genres for the movie), Production countries (a list of countries where the movie was produced), and Production companies (a list of companies involved in the movie's production).

The collected data was stored in a CSV file using csv.DictWriter. Initially, the file was created with headers to establish a consistent structure. As more movie batches were processed, data was appended to avoid overwriting, ensuring efficient storage and management of large datasets. 



**The goal of the analysis**:

The main goal of this project is to reveal the key dynamics and trends of the US film industry through a comprehensive exploration of film market data from 2000 to 2024, while helping us consolidate our core skills in Python data processing. 

This analysis is significant not only because it helps us gain insight into how the film industry has changed over the past 25 years, but also because its results are valuable for future film production, investment decisions, and market strategies. By analyzing box office revenue, company market share, and genre popularity trends, we can help production companies better understand the dynamics of the film market.

Specific goals include: 

1. Complete data scraping from a public movie database. 
2. Ensure data quality through data cleaning, including steps such as deduplication, handling missing values, and standardizing data formats. 
3. Perform data analysis and forecasting, including analyzing changes in the size of the film market, evaluating the market share of top companies, exploring the drivers of box office revenue, identifying the highest-grossing and highest-budgeted films in each decade, and analyzing the popularity trends of different film genres. 
4. Summarize and make public presentations.



**Main Source:**

- The Movie Database (TMDb) API'https://www.themoviedb.org/?language=en-US'



**Feature Libraries**: 

Before starting doing the project it's crucial to install the necessary packages by running a `requirements.txt` file. Extra libraries include:

1. Matplotlib: A Python library used for creating static, animated, and interactive visualizations in the form of graphs, charts, and plots.
   https://matplotlib.org/                                                                                               
2. NumPy: A fundamental library for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
   https://numpy.org/
3. Pandas: A powerful Python library for data manipulation and analysis, offering data structures like DataFrames and Series to handle and analyze structured data efficiently.
   https://pandas.pydata.org/
4. Requests: A Python library used for sending HTTP requests, allowing you to interact with web services by making API calls and retrieving web data easily.
   https://pypi.org/project/requests/ 



<u>**Instructions to reproduce:**</u>

**Data Scraping:**
# Python_Midterm_Project 

**Group Members**:  Maksim Korenev, Chengyang Xu, Huiwen Lian, Ningtao Xu, Vignesh Avadhanam

**Project Description**: Analysis of US movie market 2000-2024 

For this project, we collected movie data from The Movie Database (TMDb) API, focusing on films released in a specific year and country. The data collection involved two API endpoints: the Discover Movies endpoint, which was used to fetch movies based on release year and country of origin, and the Movie Details endpoint, which provided detailed information for each movie, including Budget (in dollars), Revenue (in dollars), Runtime (in minutes), Genres ( a list of genres for the movie), Production countries (a list of countries where the movie was produced), and Production companies (a list of companies involved in the movie's production).

The collected data was stored in a CSV file using csv.DictWriter. Initially, the file was created with headers to establish a consistent structure. As more movie batches were processed, data was appended to avoid overwriting, ensuring efficient storage and management of large datasets. 



**The goal of the analysis**:

The main goal of this project is to reveal the key dynamics and trends of the US film industry through a comprehensive exploration of film market data from 2000 to 2024, while helping us consolidate our core skills in Python data processing. 

This analysis is significant not only because it helps us gain insight into how the film industry has changed over the past 25 years, but also because its results are valuable for future film production, investment decisions, and market strategies. By analyzing box office revenue, company market share, and genre popularity trends, we can help production companies better understand the dynamics of the film market.

Specific goals include: 

1. Complete data scraping from a public movie database. 
2. Ensure data quality through data cleaning, including steps such as deduplication, handling missing values, and standardizing data formats. 
3. Perform data analysis and forecasting, including analyzing changes in the size of the film market, evaluating the market share of top companies, exploring the drivers of box office revenue, identifying the highest-grossing and highest-budgeted films in each decade, and analyzing the popularity trends of different film genres. 
4. Summarize and make public presentations.



**Main Source:**

- The Movie Database (TMDb) API'https://www.themoviedb.org/?language=en-US'



**Feature Libraries**: 

Before starting doing the project it's crucial to install the necessary packages by running a `requirements.txt` file. Extra libraries include:

1. Matplotlib: A Python library used for creating static, animated, and interactive visualizations in the form of graphs, charts, and plots.
   https://matplotlib.org/                                                                                               
2. NumPy: A fundamental library for numerical computing in Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
   https://numpy.org/
3. Pandas: A powerful Python library for data manipulation and analysis, offering data structures like DataFrames and Series to handle and analyze structured data efficiently.
   https://pandas.pydata.org/
4. Requests: A Python library used for sending HTTP requests, allowing you to interact with web services by making API calls and retrieving web data easily.
   https://pypi.org/project/requests/ 



<u>**Instructions to reproduce:**</u>

**Data Scraping:**

In this project, we gathered extensive movie data using The Movie Database (TMDb) API'https://www.themoviedb.org/?language=en-US', focusing on films released between 2000 and 2024 from various countries. By utilizing two key API endpoints—the Discover Movies and Movie Details endpoints—we were able to capture a comprehensive dataset on films from specific years and countries, including Budget (in dollars), Revenue (in dollars), Runtime (in minutes), Genres ( a list of genres for the movie), Production countries (a list of countries where the movie was produced), and Production companies (a list of companies involved in the movie's production)

*Basic Movie Information*
*Basic Movie Information*
Initially, we used the Discover Movies endpoint to filter movies based on their release year and country of origin and employed random sampling to capture a diverse set of movies. This approach allowed us to efficiently gather data while avoiding potential biases associated with focusing solely on the most popular films. 

*Detailed Movie Information*
*Detailed Movie Information*
After identifying movies via the Discover endpoint, we retrieved additional data using the Movie Details endpoint. For each movie, we collected detailed information such as budget (in dollars), revenue (in dollars), runtime (in minutes), genres (a list of associated genres), production countries (the countries involved in production), and production companies (the companies involved in the film's creation). This allowed us to build a richer dataset for deeper analysis.

*Data Storage:*
*Data Storage:*
The collected movie data was stored in CSV files for easy access and future analysis. Using csv.DictWriter, we initially created the file with headers to maintain a consistent structure across the dataset. As we processed batches of movies, we appended the data to the CSV file in order to avoid overwriting previous entries. This method ensured efficient storage and management of large datasets, particularly when dealing with multiple years' worth of data.

Changing the release year parameter
To cover the full scope of our project, we retrieved movie data from the TMDb API for 24 years, spanning from 2000 to 2024. By changing the release year parameter in the API calls, we were able to systematically collect data for each year. This comprehensive dataset reflects two decades of film industry trends, including financial data such as budget and revenue, as well as insights into production practices across different countries and companies.



**Data Cleaning:**
We normalized the raw data, corrected the date format, the display of the movie type and the production company, and filtered out unnecessary null values and irrelevant data to ensure that the format of each column of data was unified and in compliance with standards. We also filtered the movie data and only retained data that met specific conditions (such as a film length of more than 30 minutes and a movie produced in the United States). In this process, we integrated data from different years into a large data set to ensure that all data followed the same format and cleaning standards. At the same time, we further classified the cleaned data and generated multiple versions of the data set. To meet different analysis needs, we created a collection containing all data, a data set that only retained revenue information, and a data set with both revenue and budget information.



<u>**Findings:**</u>

**1:  Analysis of historical dynamics of US Movie market in 2000 - 2024**

In the first stage of our analysis, it was crucial to look at overall dynamics of number of films of the 25 years. For that we calculated number of films per each year of study, and the results can be seen below. It can be seen that the movie market has experienced steady growth over the whole period of study, with number of short-term decreases: a decrease in 2010, consequence of mortgage crisis of 2008-09 years and a slight decrease in 2020, caused by the problems with film production in COVID-19 pandemic. Additionally, it is necessary to mention that 2024 YTD data suggests a decrease in releases so far, but it’s too early to draw firm conclusions about the year’s overall trend.



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/Images-for-README/Images/movies_per_year.png?raw=true)

Then, we analyzed the total box office revenue of US, treating it as a proxy for overall movie market. For it we extracted the release year and combined number of movies in each year. 

Thus, in 2023 year the overall US movie market market was equal to around $12 bln. To dig deeper, we can clearly see a steady growth in box office revenue from 2000 to 2019 years coupled with a number of negligible decreases. However, the pandemic-induced disruption in 2020 caused the most significant revenue decline in modern history. The partial recovery from 2021 to 2023 suggests the industry is slowly regaining strength, though full recovery to pre-pandemic levels is still uncertain. 2024 YTD revenue indicates a slow start, but final figures may change depending on blockbuster releases later in the year.  



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/Images-for-README/Images/box_office_revenue.png?raw=true)



**2:  Analysis of top-25 US movie producers in 2000 - 2024**



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Top%2025%20Companies%20Average%20Revenue%20Share.jpg?raw=true)

In the second part, we used the processed database to focus on the top 25 production companies with the highest average revenue from 2020 to 2024. We extracted the release year, filtered the data for a specific year, calculated the average revenue for each company, and selected the top 25 companies in terms of revenue. Then, we calculated the revenue share of each company and visualized these proportions with a pie chart. Companies with a share of less than 2% are combined into the "Other" category. The chart shows the revenue distribution among the major film production companies, with each company corresponding to its revenue share. Among them, the company with the highest share is Marvel Studios, with a revenue share of 9.1%.

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Market%20Share%20Over%20Time%20for%20Top%2010%20Production%20Companies%20(2000-2024).jpg?raw=true)

We then analyzed the market share of the top 10 production companies in terms of box office revenue from 2000 to 2024. We first grouped the data by company and year, calculated the revenue share of each company each year, and filtered out the top 10 companies with the highest total revenue. Finally, the data was plotted as a stacked area chart to show the market share of each company over time. The chart shows that Walt Disney Pictures and Marvel Studios usually dominate, with Disney's market share peaking in 2019. The overall trend shows that the market share of the top companies continues to increase in important release years, indicating that the leading companies are gradually occupying a larger market share.



**3:  Highest box-office, most expensive and most profitable movies in 2000 - 2024**

We started at looking at movies of all time from analysis of the top 15 films that earned most of the revenue (as a proxy we box office revenue). "Avatar" (2009) leads the list, followed by "Avengers: Endgame" (2019) and "Avatar: The Way of Water" (2022).  Many of the films are part of major franchises, allowing us to draw a conclusion that studios create additional value to the movies production, such as marketing and conducting conferences, which increase coverage of population about the upcoming movie. Notably, "Frozen II" (2019) and "The Lion King" (2019) are among the highest-grossing animated films on the list.

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/top_revenue_films.png?raw=true)

Additionally, based on that graph we can infer population's preferences of movies. That being said, consumers have a strong preference for blockbuster franchises and visually immersive films, as seen in the dominance of sequels, superhero movies, and animated features. Finally, the presence of animated films like "Frozen II" and "Inside Out 2" shows a broad appeal for family-friendly content.

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/top_budget_films.png?raw=true)

The high production costs reflected in the graph suggest that film companies are responding to audience demand by investing heavily in large-scale, visually immersive experiences. Films like *Avatar: The Way of Water*, *Avengers*, and *Star Wars* sequels have massive budgets, indicating that studios are willing to allocate substantial resources to meet the expectations for advanced special effects, cutting-edge CGI, and action-packed narratives. This aligns with audience preferences for visually spectacular and high-stakes films, especially within established franchises.

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/top_profitability_films.png?raw=true)

As a result, the most profitable films, such as Avatar (2009) and Avengers: Endgame (2019), highlight the significant financial return that blockbuster films can generate relative to their production costs. Despite large budgets, these films achieve high profitability, indicating that the massive investments in production and marketing are justified by the substantial global box office receipts. Franchise films dominate the list, showing that audiences’ willingness to pay for familiar, high-quality content translates into strong returns on investment for studios.


**4:  Linear regression of box-office revenue**

Correlation analysis-

We first conducted simple correlation between some key variables. The highest correlation is 0.76 which is the correlation between revenue and vote count, and revenue and budget. Then we have the correlation between vote count and budget which is 0.62.

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/regression_analysis_graphs/correlation_map.png?raw=true)

OLS results - 
$$
TotalBudget = 1.5*Budget
$$
The below shows output from simple linear regression of revenue on total_budget. I found information online that marketing and distribution costs about 50% of production budget. 



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/regression_analysis_graphs/Regression_OLS%20results.png?raw=true)

**5.**

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/roipergenre.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/roiperquarter.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/votecountpergenre.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/votecountperquarter.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/avgbudgetpergenre.jpg?raw=true)



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/totalbudgetperquarter.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/numbermoviespergenre.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/numbermoviesquarter.jpg?raw=true)

**6: Profitability Analysis**

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/prob_avg_vote.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/prob_runtime.jpg?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/prob_vote_count.jpg?raw=true)



**7:  Revenue Trends by Movie Genre**

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Revenue%20Trends%20by%20Movie%20Genre.jpg?raw=true)

We processed and used our cleaned database to analyze the revenue trends by genre. We first extracted the release year, and then grouped and summarized the revenue of each genre each year by genre and year. Then, we pivoted the data into a table, with each column representing a genre and each row corresponding to a year, and finally drew a line chart of the total annual revenue trends of each genre. The line chart shows the trend of revenue by genre over time. It is worth noting that the action and adventure genres have the highest revenue, especially the action genre, which reached its peak in 2020, exceeding US$8 billion.



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Box%20Office%20Revenue%20Share%20by%20Genre.jpg?raw=true)

We then analyzed the share of box office revenue by genre from 2000 to 2024. We first calculated the total revenue for each year and determined the annual market share for each genre. We selected the 10 genres with the highest total revenue and combined all other genres into the "Other" category to simplify the analysis. Finally, the data was plotted as a stacked bar chart to show the annual revenue share of each genre over time. This chart shows the contribution of different types of movies to the total box office revenue each year. Obviously, the action, adventure, and animation genres have always had a large market share over time.


**8:  Genre Revenue Share in 2000, 2012, 2020 and 2024**

For the sixth part, first, we extract the release year of each movie. Then we group by genre and year and calculate the revenue. We select specific years to draw pie charts to show the revenue share of different movie genres in these years. Among them, in 2020, we want to observe whether covid-19 has an impact on the film industry. For each selected year of data, we calculate the percentage of each genre's revenue in the total annual revenue and use the function to draw a pie chart. Each pie chart shows the revenue distribution of each movie genre in a specified year, which helps to observe the changing trends of popular movie genres in different periods. In 2000, comedy had the highest share of 27.4%, followed by adventure (16.5%) and drama (13.3%). In 2012: Science fiction leads with a share of 17.3%, followed by animation (16.3%) and comedy (14.4%), indicating a shift in popular genres. In 2020, the thriller category dominated for the first time, accounting for 25.0%, followed by action (23.2%) and animation (18.6%). In 2024, animation continued to grow, accounting for 32.1%, while action (28.1%) and science fiction (10.7%) also still accounted for a large share.

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Genre%202000.png?raw=true)



![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Genre%202012.png?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Genre%202020.png?raw=true)

![Alt text](https://github.com/WinnieLian/python_midterm_program/blob/main/Images/Genre%202024.png?raw=true)

**Conclusion**

Through a multi-angle analysis of the US film market, this project shows the development trends and market dynamics of the film industry over the past two decades. We found that the COVID-19 epidemic has dealt a severe blow to the film industry, but the market is gradually recovering and is expected to pick up further in the next few years. Series and superhero movies remain the most popular film genres among audiences. Their high revenue and high investment prove that film companies can get huge returns on investment by building a strong brand effect. In addition, moviegoers' preferences for different types of movies are changing year by year. Although action, adventure and animation have always dominated the market, the market share of animation has continued to rise in recent years, especially with its wide appeal among family audiences. From the perspective of production companies, production companies that dominate the US film market, such as Disney and Marvel Studios, still have a large share in the market, which shows that the influence of large companies in the film market is gradually increasing.



**Limitations** 

1. Our data coverage is limited. Our analysis covers only 25 years of data between 2000 and 2024, so it fails to reflect earlier or possible future trends. This may cause us to miss some important historical events or long-term trends. 
2. The accuracy and completeness of our data sources may be limited. Our data is obtained from public data sources (TMDB and other movie databases), which may be missing or inaccurate. In addition, data from some years may be more detailed or complete than other years, which will affect the reliability of the results. 
3. We ignored the analysis of critics ratings and reviews. Additionally, we did not conduct any qualitative interviews (didn't ask face-to-face questions to the critics as well as consumers). 
4. This project mainly uses simple summary analysis methods, rather than more complex machine learning models for in-depth analysis. Therefore, the analysis of the relationship between multiple variables may not be in-depth and comprehensive enough.



**A discussion of extensions of data**

1. Introduce machine learning models for box office prediction. In the future, linear regression, random forest, support vector machine, etc. can be used to predict the box office performance of movies. By training models, we can predict the box office revenue of new movies.
2. Global film market analysis. The current analysis focuses on the US market, but in the future it can be expanded to the global market to study audience preferences and market dynamics in different countries and regions.
3. In-depth analysis of the relationship between film costs and returns. Analyze the difference in profitability between high-budget and low-budget films through historical data, analyze which types of films have the greatest returns at different budget levels, etc.

