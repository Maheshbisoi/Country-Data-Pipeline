
import requests
from bs4 import BeautifulSoup

URL = "https://www.scrapethissite.com/pages/simple/"

def scrape_countries():
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    countries = []

    for item in soup.select(".country")[:20]:
        country = {
            "name": item.select_one(".country-name").get_text(strip=True),
            "capital": item.select_one(".country-capital").get_text(strip=True),
            "population": int(item.select_one(".country-population").get_text(strip=True)),
            "area": float(item.select_one(".country-area").get_text(strip=True))
        }
        countries.append(country)

    return countries

if __name__ == "__main__":
    data = scrape_countries()
    print(f"Total countries scraped: {len(data)}")

    for country in data:
        print(country)
