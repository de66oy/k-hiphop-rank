import json
import requests
from bs4 import BeautifulSoup

# Example: Scrapping a public chart or using a placeholder for logic
# In a real scenario, you'd use the YouTube Data API or a Melon scraper.
def get_artist_data():
    # This is a mock-up of the data structure
    artists = [
        {"name": "Changmo", "views": 150000000, "link": "changmo.html"},
        {"name": "Beenzino", "views": 120000000, "link": "beenzino.html"},
        {"name": "Zico", "views": 200000000, "link": "zico.html"}
    ]
    # Sort by views descending
    return sorted(artists, key=lambda x: x['views'], reverse=True)

if __name__ == "__main__":
    ranked_data = get_artist_data()
    with open('data.json', 'w') as f:
        json.dump(ranked_data, f, indent=4)
