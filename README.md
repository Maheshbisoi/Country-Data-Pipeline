# Country Data Pipeline & Analytics System

## About
A Python project that scrapes data about 20 countries, stores it in an SQLite database, provides a REST API, exports data to CSV, and generates a chart.

## Technologies
- Python
- BeautifulSoup and Requests
- SQLite
- FastAPI
- Pandas
- Matplotlib

## Features
- Scrapes country name, capital, population, and area.
- Stores data in SQLite.
- Supports CRUD operations through FastAPI.
- Exports data to CSV.
- Calculates basic statistics.
- Generates a population-versus-area chart.

## How to Run

Install dependencies:

    pip install -r requirements.txt

Scrape and save country data:

    python seed_database.py

Start the API:

    python -m uvicorn main:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs

In a second terminal, run the client:

    python client.py

Generate analytics and the chart:

    python analytics.py

## Output Files
- countries.db — SQLite database
- exported_countries.csv — Country data in CSV format
- population_vs_area.png — Scatter plot

## Data Source
https://www.scrapethissite.com/pages/simple/
