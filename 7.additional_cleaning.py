import pandas as pd

def additional_cleaning(dataframe):
    dataframe['total_budget'] = 1.5*dataframe['budget']
    dataframe["release_date"] = pd.to_datetime(dataframe["release_date"])

    dataframe["release_year"] = dataframe["release_date"].dt.year
    dataframe['release_month'] = dataframe['release_date'].dt.month
    release_quarter = []

    for values in dataframe['release_month']:
        if values in (1,2,3):
            release_quarter.append({'release_quarter':1})
        elif values in (4,5,6):
            release_quarter.append({'release_quarter':2})
        elif values in (7,8,9):
            release_quarter.append({'release_quarter':3})
        else:
            release_quarter.append({'release_quarter':4})
    
    df_release_quarter  = pd.DataFrame(release_quarter)

    df_with_release_quarter = pd.merge(dataframe, df_release_quarter, left_index=True, right_index=True)
    
    return df_with_release_quarter


