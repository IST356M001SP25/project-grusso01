import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    df.columns = df.columns.str.strip().str.upper()

    df = df.rename(columns={
        'REFUSETONSCOLLECTED': 'REFUSE_TONS_COLLECTED',
        'MGPTONSCOLLECTED': 'MGP_TONS_COLLECTED',
        'PAPERTONSCOLLECTED': 'PAPER_TONS_COLLECTED'
    })

    return df

def compute_metrics(df):
    df['RECYCLABLE_TONS_COLLECTED'] = df['PAPER_TONS_COLLECTED'] + df['MGP_TONS_COLLECTED']

    df['TOTAL_WASTE_TONS'] = df['RECYCLABLE_TONS_COLLECTED'] + df['REFUSE_TONS_COLLECTED']
    df = df[df['TOTAL_WASTE_TONS'] > 0]

    df['CAPTURE_RATE'] = df['RECYCLABLE_TONS_COLLECTED'] / df['TOTAL_WASTE_TONS']

    return df

if __name__ == '__main__':
    raw_df = load_and_clean_data('cache/cleaned_tonnage_data.csv')
    transformed_df = compute_metrics(raw_df)

    transformed_df.to_csv('cache/cleaned_tonnage_data.csv', index=False)
    print(" Updated data with CAPTURE_RATE saved to cache/cleaned_tonnage_data.csv")