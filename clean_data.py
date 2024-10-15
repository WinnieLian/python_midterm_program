import pandas as pd
import os

base_path = r'/mnt/d/python 项目/project1/raw_data'

# data_clean functions 
def clean_data(df):
    df.columns = df.columns.str.strip()
    
    df.loc[:, 'release_date'] = pd.to_datetime(df['release_date'], errors='coerce').dt.strftime('%Y-%m-%d')
    df.loc[:, 'genres'] = df['genres'].apply(lambda x: x.split(',')[0] if isinstance(x, str) and len(x) > 0 else "Non-Specified")
    df.loc[:, 'production_countries'] = df['production_countries'].apply(lambda x: x.split(',')[0].strip("[]' ") if isinstance(x, str) and len(x) > 0 else None)
    df = df[df['production_countries'] == 'United States of America']
    df.loc[:, 'production_companies'] = df['production_companies'].apply(lambda x: x.split(',')[0].strip("[]' ") if isinstance(x, str) and len(x) > 0 else None)
    df = df[df['runtime'] >= 30]
    df = df.drop_duplicates(subset='title', keep='first')
    
    return df

# Loop through each year, process the data, and combine it
years = ['2024', '2023', '2022', '2021', '2020',
         '2019', '2018', '2017', '2016', '2015',
         '2014', '2013', '2012', '2011', '2010',
         '2009', '2008', '2007', '2006', '2005',
         '2004', '2003', '2002', '2001', '2000']
combined_data = pd.DataFrame()

for year in years:
    file_path = os.path.join(base_path, f'movies_{year}_filtered.csv')
    
    if os.path.exists(file_path):
        movies = pd.read_csv(file_path, encoding='ISO-8859-1')

        movies.columns = movies.columns.str.strip()

        if 'revenue' in movies.columns:
            movies_cleaned = clean_data(movies)
            combined_data = pd.concat([combined_data, movies_cleaned], ignore_index=True)
        else:
            print(f"Error")
    else:
        print(f"Error")