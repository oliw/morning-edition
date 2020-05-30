import argparse
import requests
from bs4 import BeautifulSoup

# Morning Edition Scraper
#
# Given the URL to a Morning Edition Page this script
# fill parser the contents of that site and extract any song detaiils


def getTracks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    songs = soup.find_all("div", class_="song-meta-wrap")
    tracks = []

    for song in songs:
        title_and_artist = song.findAll('span')
        title = title_and_artist[0].get_text()
        artist = title_and_artist[1].get_text()
        tracks.append({"title": title, "artist": artist})
    return tracks


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find all the songs played in a morning edition episode')
    parser.add_argument('episode_url', metavar='url', type=str,
                        help='A url to the morning edition episode https://www.npr.org/programs/morning-edition/2020/05/14/855836328')
    args = parser.parse_args()
    tracks = getTracks(args.episode_url)
    for track in tracks:
        print(f"{track['title']} by {track['artist']}")
