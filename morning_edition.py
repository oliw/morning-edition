import argparse
from episode_lister import getRecentEpisodeUrls
from song_lister import getTracks

# Morning Edition Scraper
#
# Given the URL to a Morning Edition Page this script
# fill parser the contents of that site and extract any song detaiils


parser = argparse.ArgumentParser(
    description='Find all the songs played in recent morning edition episodes')
args = parser.parse_args()

episode_urls = getRecentEpisodeUrls(7)

for episode_url in episode_urls:
    print(f'// Songs from {episode_url}')
    tracks = getTracks(episode_url)
    for track in tracks:
        print(f"{track['title']} by {track['artist']}")
