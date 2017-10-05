import requests
# from urllib.parse import urlparse
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup as soup

def audio_spider():
    url = 'http://freakonomics.com/archive/'
    url_queue = retrieve_html_source(url)
    mp3_url_group = url_queue.find_all(class_ = 'green-title')
    tag_queue = []

    for mp3_url in mp3_url_group:
        link = mp3_url.find('a')
        if link:
            tag_queue.append(link)

    return tag_queue

def send_url(tags):
    for tag in tags:
        send_download_link(tag['href'])

def send_download_link(link):
    url_queue = retrieve_html_source(link)
    download_file_url = url_queue.find(class_ = 'download_wrapper').find('a')
    download_file(download_file_url['href'])

def download_file(url):
    split = urllib.parse.urlsplit(url)
    filename = split.path.split("/")[-1]
    urllib.request.urlretrieve(url, filename)

def retrieve_html_source(url):
    source_html = requests.get(url)
    url_queue = soup(source_html.content, 'html.parser')
    return url_queue

send_url(audio_spider())