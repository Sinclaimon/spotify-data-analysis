def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()  # Remove missing values
    df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime
    return df

def transform_data(df):
    # Example transformation: adding a new column for streaming duration
    df['streaming_duration'] = df['end_time'] - df['start_time']
    return df