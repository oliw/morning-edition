import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Morning Edition Show Finder
#
# List URLs of recent morning edition episodes


def getRecentEpisodeUrls(num_shows):
    starting_url = "https://www.npr.org/programs/morning-edition/archive"
    return collectAndFollowUrl(starting_url, num_shows)


def collectAndFollowUrl(url, num_shows):
    shows = []
    if num_shows <= 0:
        return shows
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    show_links = soup.findAll("a", class_="program-show__full-show")
    show_hrefs = [link['href'] for link in show_links]
    shows += show_hrefs[0:num_shows]
    if len(shows) >= num_shows:
        return shows
    # Proceed to next
    next_page_path = soup.find("div", class_="scrolllink").find("a")['href']
    o = urlparse(url)
    next_page_url = f'{o.scheme}://{o.netloc}{next_page_path}'
    return shows + collectAndFollowUrl(next_page_url, num_shows-len(shows))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find all the songs played in a morning edition episode')
    parser.add_argument('num_episodes', metavar='num_episodes',
                        type=int, help='How many of the most recent shows to fetch')
    args = parser.parse_args()
    episode_urls = getRecentEpisodeUrls(args.num_episodes)
    for url in episode_urls:
        print(url)
