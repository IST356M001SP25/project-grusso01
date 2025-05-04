import pandas as pd
import os

def load_raw_tonnage_data(cache_path='cache/monthly_tonnage_raw.csv'):
    """Loads the raw DSNY monthly tonnage data from CSV."""
    if not os.path.exists(cache_path):
        raise FileNotFoundError(f"CSV file not found at: {cache_path}")
    
    df = pd.read_csv(cache_path)
    return df

def clean_tonnage_data(df):
    """Keeps relevant columns and filters out rows with nulls or unnecessary data."""
    df_clean = df[['BOROUGH', 'MONTH', 'REFUSETONSCOLLECTED', 
                   'MGPTONSCOLLECTED', 'PAPERTONSCOLLECTED']].copy()
    
    df_clean.dropna(subset=['BOROUGH', 'MONTH'], inplace=True)

    return df_clean

def save_clean_data(df, out_path='cache/cleaned_tonnage_data.csv'):
    """Saves cleaned DataFrame to CSV."""
    df.to_csv(out_path, index=False)

if __name__ == '__main__':
    raw_df = load_raw_tonnage_data()
    cleaned_df = clean_tonnage_data(raw_df)
    save_clean_data(cleaned_df)
    print("Done cleaning.")