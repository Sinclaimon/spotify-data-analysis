import pandas as pd
import glob
import os


def load_data(file_path):
    """Load raw data from JSON files."""
    all_files = glob.glob(file_path)
    df_list = [pd.read_json(file) for file in all_files]
    return pd.concat(df_list, ignore_index=True), all_files


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
    """Transform the data to extract various insights."""
    # Extract date from timestamp
    df["date"] = df["timestamp"].dt.date

    # Aggregate data by date for daily streams
    daily_streams = df.groupby("date").size().reset_index(name="streams")

    # Calculate total play time per day
    total_play_time_per_day = (
        df.groupby("date")["ms_played"].sum().reset_index(name="total_play_time_ms")
    )

    # Calculate total play time per artist
    total_play_time_per_artist = (
        df.groupby("master_metadata_album_artist_name")["ms_played"]
        .sum()
        .reset_index(name="total_play_time_ms")
    )

    # Count play count per track
    play_count_per_track = (
        df.groupby("master_metadata_track_name").size().reset_index(name="play_count")
    )
    play_count_per_track = play_count_per_track.sort_values(
        "play_count", ascending=False
    )

    # Count play count per album
    play_count_per_album = (
        df.groupby("master_metadata_album_album_name")
        .size()
        .reset_index(name="play_count")
    )
    play_count_per_album = play_count_per_album.sort_values(
        "play_count", ascending=False
    )

    return (
        daily_streams,
        total_play_time_per_day,
        total_play_time_per_artist,
        play_count_per_track,
        play_count_per_album,
    )


def save_data(dfs, file_paths):
    """Save the processed data to CSV files."""
    for df, file_path in zip(dfs, file_paths):
        df.to_csv(file_path, index=False)


def main():
    # Load raw data
    raw_data_path = "data/raw/Spotify Extended Streaming History/Streaming_History_Audio_2016-2018_0.json"
    df, all_files = load_data(raw_data_path)

    # Clean data
    df = clean_data(df)
    print("data after clean: ", df)

    # Transform data
    (
        daily_streams,
        total_play_time_per_day,
        total_play_time_per_artist,
        play_count_per_track,
        play_count_per_album,
    ) = transform_data(df)

    # Extract the base name from the first raw data file
    if all_files:
        first_file = os.path.basename(all_files[0])
        base_name, _ = os.path.splitext(first_file)
        base_name = base_name.replace("Streaming_History_Audio_", "")
    else:
        base_name = "default"

    print("Base name extracted from the raw data path:", base_name)

    # Construct the processed data file names
    processed_data_paths = [
        f"data/processed/streaming_history_daily_streams_{base_name}.csv",
        f"data/processed/streaming_history_total_play_time_{base_name}.csv",
        f"data/processed/streaming_history_total_play_time_per_artist_{base_name}.csv",
        f"data/processed/streaming_history_play_count_per_track_{base_name}.csv",
        f"data/processed/streaming_history_play_count_per_album_{base_name}.csv",
    ]

    # Save processed data
    save_data(
        [
            daily_streams,
            total_play_time_per_day,
            total_play_time_per_artist,
            play_count_per_track,
            play_count_per_album,
        ],
        processed_data_paths,
    )
    print("Processed data saved.")


if __name__ == "__main__":
    main()
