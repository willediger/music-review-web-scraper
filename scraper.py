__author__ = 'Will'

from collections import defaultdict
from lxml import html
import requests

page = requests.get('http://www.avclub.com/music/')
tree = html.fromstring(page.text)

grades = tree.xpath('//*[@id="pane-01"]/ul/li/div[1]/a/text()')
grades = [grade.strip() for grade in grades]

albums = tree.xpath('//*[@id="pane-01"]/ul/li/div[2]/div/text()')
albums = [album.strip() for album in albums]

artists = tree.xpath('//*[@id="pane-01"]/ul/li/div[2]/h2/a/span/text()')
artists = [artist.strip() for artist in artists]

albums_artists = list(zip(albums, artists))

albums_artists_grades = dict(zip(albums_artists, grades))


def good_albums():
    return list({k: v for k, v in albums_artists_grades.items() if v == 'A' or v == 'A-' or v == 'A+'}.keys())

print(good_albums())
