__author__ = 'Will'

from collections import defaultdict
from lxml import html
import requests
import utils

text_fn = '/text()'

grabbed_albums_tbl = 'grabbed_albums'
new_albums_tbl = 'new_albums'
artist_field = 'artist_name'
album_field = 'album_name'
field_type = 'text'

def tree(url):
    page = requests.get(url)
    _tree = html.fromstring(page.text)
    return _tree

def albums_artists(html_tree, album_xpath, artist_xpath):
    album_list = html_tree.xpath(album_xpath + text_fn)
    album_list = [album.strip() for album in album_list]

    artist_list = html_tree.xpath(artist_xpath + text_fn)
    artist_list = [artist.strip() for artist in artist_list]

    albums_artists = list(zip(album_list, artist_list))
    return albums_artists

def album_grade(html_tree, grade_xpath):
    grade_list = html_tree.xpath(grade_xpath + text_fn)
    grade_list = [grade.strip() for grade in grade_list]

    return grade_list

def good_albums(albums_artists_grades):
    return list({k: v for k, v in albums_artists_grades.items() if v == 'A' or v == 'A-' or v == 'A+'}.keys())

avclub_tree = tree('http://www.avclub.com/music/')
avclub_albums_artists_full = albums_artists(avclub_tree, '//*[@id="pane-01"]/ul/li/div[2]/div',
                                            '//*[@id="pane-01"]/ul/li/div[2]/h2/a/span')
avclub_album_grades_full = album_grade(avclub_tree, '//*[@id="pane-01"]/ul/li/div[1]/a')
avclub_albums_artists_grades = dict(zip(avclub_albums_artists_full, avclub_album_grades_full))
avclub_good_albums = good_albums(avclub_albums_artists_grades)

pf_tree = tree('http://pitchfork.com/reviews/best/albums/')
pf_albums_artists = albums_artists(pf_tree, '//*[@id="main"]/ul/li/div[2]/a/h2',
                                   '//*[@id="main"]/ul/li/div[2]/a/h1')

all_albums_artists = avclub_good_albums + pf_albums_artists

print(all_albums_artists)
