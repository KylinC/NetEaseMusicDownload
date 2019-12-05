import requests
from bs4 import BeautifulSoup
import urllib.request

class Downloader:
    def __init__(self,download_path):
        self.tamplate_url = "http://music.163.com/song/media/outer/url?id="
        self.buck_list = []
        self.download_path = download_path

    def download(self,song_id,song_name="aim",song_singer="aim"):
        music_url = self.tamplate_url + song_id + ".mp3"
        song_path = '%s/%s.mp3'% (self.download_path,song_name+"-"+song_singer)
        urllib.request.urlretrieve(music_url,song_path)

if __name__ == '__main__':
    a = Downloader("./download")
    a.download("1079429","Make You Feel My Love","Bob Dylan")

    