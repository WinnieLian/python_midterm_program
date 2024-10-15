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