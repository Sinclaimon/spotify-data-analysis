import pandas as pd


def load_data(file_path):
    """Load raw data from a CSV file."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Clean the raw data."""
    # Replace empty strings with NaN
    df.replace("", pd.NA, inplace=True)

    # Handle missing values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert data types if necessary
    # Example: Convert 'timestamp' column to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


def transform_data(df):
    """Transform the data."""
    # Example: Extract date and time from timestamp
    df["date"] = df["timestamp"].dt.date
    df["time"] = df["timestamp"].dt.time

    # Example: Aggregate data by date
    daily_streams = df.groupby("date").size().reset_index(name="streams")

    return daily_streams


def save_data(df, file_path):
    """Save the processed data to a CSV file."""
    df.to_csv(file_path, index=False)


def main():
    # Load raw data
    raw_data_path = "data/raw/spotify_streaming_data.csv"
    df = load_data(raw_data_path)

    # Clean data
    df = clean_data(df)

    # Transform data
    df = transform_data(df)

    # Save processed data
    processed_data_path = "data/processed/spotify_streaming_data_processed.csv"
    save_data(df, processed_data_path)


if __name__ == "__main__":
    main()
