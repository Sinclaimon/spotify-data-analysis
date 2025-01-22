import pandas as pd
import glob
import os


def load_data(file_path):
    """Load raw data from JSON files."""
    all_files = glob.glob(file_path)
    df_list = [pd.read_json(file) for file in all_files]
    return pd.concat(df_list, ignore_index=True)


def clean_data(df):
    """Clean the raw data."""
    # Print column names for debugging
    print("Columns in the DataFrame:", df.columns)

    # Rename 'ts' column to 'timestamp'
    if "ts" in df.columns:
        df.rename(columns={"ts": "timestamp"}, inplace=True)

    # Replace empty strings with NaN
    df.replace("", pd.NA, inplace=True)
    print("Data before dropna clean:\n", df.head())

    # Print the count of missing values in each column
    print("Missing values in each column:\n", df.isna().sum())

    # Handle missing values, only considering specific columns
    df = df.dropna(subset=["timestamp", "ms_played", "master_metadata_track_name"])

    # Print the DataFrame after dropping missing values
    print("Data after dropna clean:\n", df.head())

    # Remove duplicates
    df = df.drop_duplicates()

    # Check if 'timestamp' column exists
    if "timestamp" in df.columns:
        # Convert data types if necessary
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    else:
        raise KeyError("The 'timestamp' column is missing from the data.")

    return df


def transform_data(df):
    """Transform the data."""
    # Extract date from timestamp
    df["date"] = df["timestamp"].dt.date

    # Aggregate data by date
    daily_streams = df.groupby("date").size().reset_index(name="streams")

    return daily_streams


def save_data(df, file_path):
    """Save the processed data to a CSV file."""
    df.to_csv(file_path, index=False)


def main():
    # Load raw data
    raw_data_path = "data/raw/Spotify Extended Streaming History/Streaming_History_Audio_2016-2018_0.json"
    df = load_data(raw_data_path)

    # Clean data
    df = clean_data(df)
    print("data after clean: ", df)
    # Transform data
    df = transform_data(df)

    # Extract the base name from the raw data path
    base_name = (
        os.path.basename(raw_data_path)
        .replace("Streaming_History_Audio_", "")
        .replace("*.json", "")
    )

    print("Base name extracted from the raw data path:", base_name)
    # Construct the processed data file name
    processed_data_path = f"data/processed/streaming_history{base_name}.csv"

    # Save processed data
    save_data(df, processed_data_path)
    print("processed data: ", df)


if __name__ == "__main__":
    main()
