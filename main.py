from bs4 import BeautifulSoup
import requests
import sys
from datetime import datetime


date = input("Enter the date (YYYY-MM-DD) to retrieve Billboard Hot 100: ")


try:
    datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("Error: Incorrect date format. Please use YYYY-MM-DD.")
    sys.exit(1)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}


url = f"https://www.billboard.com/charts/hot-100/{date}"

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Raise an error for bad status codes
except requests.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Select song entry elements
# The selector targets each song entry container
song_entries = soup.select("li.o-chart-results-list__item")


songs = []


for entry in song_entries:
    # Extract song title
    title_tag = entry.select_one("h3#title-of-a-story")
    # Extract artist name
    artist_tag = entry.select_one("span.c-label.a-no-trucate")

    if title_tag and artist_tag:
        title = title_tag.get_text(strip=True)
        artist = artist_tag.get_text(strip=True)

        # Skip entries that are not actual songs
        if any(keyword in title.lower() for keyword in ["songwriter(s)", "producer(s)", "imprint/promotion label"]):
            continue

        songs.append({"title": title, "artist": artist})

        # Stop after collecting 10 songs
        if len(songs) == 10:
            break


if not songs:
    print("No songs were extracted. The page structure might have changed.")
    sys.exit(1)

# Print the first 10 songs with their artists
print("\nBillboard Hot 100 Songs:")
for idx, song in enumerate(songs, start=1):
    print(f"{idx}. {song['title']} by {song['artist']}")
