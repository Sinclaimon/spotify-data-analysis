def plot_streaming_trends(data):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='date', y='streams', hue='artist')
    plt.title('Streaming Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Streams')
    plt.xticks(rotation=45)
    plt.legend(title='Artist')
    plt.tight_layout()
    plt.show()

def plot_top_artists(data, top_n=10):
    import matplotlib.pyplot as plt
    import seaborn as sns

    top_artists = data.groupby('artist')['streams'].sum().nlargest(top_n).reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_artists, x='streams', y='artist', palette='viridis')
    plt.title(f'Top {top_n} Artists by Total Streams')
    plt.xlabel('Total Streams')
    plt.ylabel('Artist')
    plt.tight_layout()
    plt.show()

def plot_genre_distribution(data):
    import matplotlib.pyplot as plt
    import seaborn as sns

    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, y='genre', order=data['genre'].value_counts().index, palette='pastel')
    plt.title('Distribution of Genres')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.show()