from NetEaseDown.Downloader import Downloader
from NetEaseDown.Searcher import Search

class Scheduler:
    def __init__(self,download_path):
        self.downloader = Downloader(download_path)
        self.searcher = Search()
        self.search_span = 100

    def download_bydetail(self,song_name,song_singer):
        search_list = self.searcher.search_song(song_name+" "+song_singer,limit=10)
        aim_id = search_list[0][0]
        aim_id = str(aim_id)
        aim_songname = search_list[0][1]
        aim_songsinger = search_list[0][2]
        self.downloader.download(aim_id,aim_songname,aim_songsinger)

    def download_bysongname(self,song_name,download_num=10):
        search_list = self.searcher.search_song(song_name,limit=10)
        print(len(search_list))
        for idx in range(download_num):
            aim_id = search_list[idx][0]
            aim_id = str(aim_id)
            aim_songname = search_list[idx][1]
            aim_songsinger = search_list[idx][2]
            self.downloader.download(aim_id,aim_songname,aim_songsinger)

    def download_bysingername(self,song_singer,download_num=10):
        search_list = self.searcher.search_song(song_singer,limit=10)
        for idx in range(download_num):
            aim_id = search_list[idx][0]
            aim_id = str(aim_id)
            aim_songname = search_list[idx][1]
            aim_songsinger = search_list[idx][2]
            self.downloader.download(aim_id,aim_songname,aim_songsinger)

    def download_bylist(self):
        pass

if __name__ == "__main__":
    a = Scheduler("./download")
    a.download_bydetail("Make You Feel My Love","Bob Dylan")
    a.download_bysongname("the portrait")