
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/countries"


def main():
    print("Fetching country data from API...")

    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    countries = response.json()
    df = pd.DataFrame(countries)

    print("\nCountry Data:")
    print(df.to_string(index=False))

    df.to_csv("exported_countries.csv", index=False)

    print("\nTotal countries:", len(df))
    print("CSV exported successfully!")


if __name__ == "__main__":
    main()
