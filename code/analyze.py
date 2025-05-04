import pandas as pd

def load_data(path='cache/cleaned_tonnage_data.csv'):
    """Load the cleaned + transformed recycling data."""
    df = pd.read_csv(path)
    return df

def prepare_summary(df):
    """Filter, extract year, and compute average capture rate by borough/year."""
    df = df[df['CAPTURE_RATE'].notna()]
    df = df[df['TOTAL_WASTE_TONS'] > 0]

    df['YEAR'] = df['MONTH'].str[:4].astype(int)

    summary = (
        df.groupby(['BOROUGH', 'YEAR'])['CAPTURE_RATE']
        .mean()
        .reset_index()
        .rename(columns={'CAPTURE_RATE': 'AVG_CAPTURE_RATE'})
    )
    return summary

def save_summary(df, path='cache/borough_capture_summary.csv'):
    df.to_csv(path, index=False)
    print(f"Summary saved to {path}")

if __name__ == '__main__':
    df = load_data()
    summary_df = prepare_summary(df)
    save_summary(summary_df)
    print(summary_df.head())