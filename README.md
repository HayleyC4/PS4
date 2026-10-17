# PS4

# NASA Astronomy Picture of the Day API Project

## Overview

This project uses NASA's Astronomy Picture of the Day (APOD) API
to retrieve and analyze astronomy-related media entries.

## Research Question

How does the length of NASA's Astronomy Picture of the Day (APOD) explanations vary over a 30-day period?

## Data Source

NASA Open APIs — Astronomy Picture of the Day (APOD)

Documentation: https://api.nasa.gov/

API endpoint:
https://science.nasa.gov/wp-json/wp/v2/apod-basic/

## Methods

1. Send a GET request to the NASA APOD API using Python.
2. Retrieve up to 10 randomly selected entries.
3. Extract each entry's date, title, and media type.
4. Organize the selected fields into a pandas DataFrame.
5. Count the number of entries for each media type.
6. Display the selected data in a table.
7. Create a bar graph to visualize the media type counts.
8. Export the selected data to a CSV file.

## Libraries

- requests
- pandas
- matplotlib

## How to Run

Install the required packages:

    pip install -r requirements.txt

Run the script:

    python nasa_apod_project.py

For higher API usage limits, set the NASA_API_KEY
environment variable to your own NASA API key.

## Outputs

- A table of selected APOD entries
- A summary of media type counts
- apod_results.csv
- apod_media_types.png
