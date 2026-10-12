
from scraper import scrape_countries
from database import CountryDatabaseManager


def main():
    print("Starting country database setup...")

    countries = scrape_countries()
    print(f"Successfully scraped {len(countries)} countries!")

    db = CountryDatabaseManager()
    db.insert_many(countries)

    saved_countries = db.get_all_countries()

    print("Countries saved to countries.db successfully!")
    print(f"Total countries in database: {len(saved_countries)}")

    print("\nFirst 5 database records:")
    for country in saved_countries[:5]:
        print(country)


if __name__ == "__main__":
    main()
