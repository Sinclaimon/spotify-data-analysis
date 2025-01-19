# Spotify Data Analysis Project

This project is designed for analyzing and visualizing Spotify streaming data. It includes functionalities for loading, processing, and visualizing the data to gain insights into streaming trends, popular artists, and genre distributions.

## Project Structure

- **data/**
  - **raw/**: Contains the raw Spotify streaming data files (CSV or JSON format).
  - **processed/**: Holds the processed data files after cleaning and transforming the raw data.
  
- **notebooks/**
  - **analysis.ipynb**: A Jupyter notebook for data analysis and visualization, including code for loading data, performing analysis, and generating visualizations.

- **src/**
  - **data_processing.py**: Functions for loading, cleaning, and processing the raw Spotify streaming data. Key functions include:
    - `load_data`
    - `clean_data`
    - `transform_data`
  
  - **visualization.py**: Responsible for creating visualizations of the processed data. Key functions include:
    - `plot_streaming_trends`
    - `plot_top_artists`
    - `plot_genre_distribution`
  
  - **utils.py**: Utility functions for data validation and helper functions. Key functions include:
    - `save_to_csv`
    - `load_from_csv`
    - `generate_summary_statistics`

- **requirements.txt**: Lists the Python dependencies required for the project, including:
  - pandas
  - matplotlib
  - seaborn
  - Jupyter

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage Examples

- To load and clean the data, use the functions defined in `data_processing.py`.
- For visualizations, utilize the functions in `visualization.py` to create insightful plots.
- Use the Jupyter notebook `analysis.ipynb` for an interactive analysis experience.

## License

This project is licensed under the MIT License.