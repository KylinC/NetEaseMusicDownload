from NetEaseDown.Scheduler import Scheduler
import sys
import io

download_path = "./download"

schedule = Scheduler(download_path)

try:
    search_songname = str(input("SongName:(or Empty)"))
    search_singername = str(input("SingerName:(or Empty)"))

    if(search_songname and search_singername):
        schedule.download_bydetail(search_songname,search_singername)
        print("complete!")
    elif(search_songname):
        print("-----Download By Song Name-----")
        span_number = int(input("Download_Number:"))
        schedule.download_bysongname(search_songname,span_number)
        print("complete!")
    elif(search_singername):
        print("-----Download By Singer Name-----")
        span_number = int(input("Download_Number:"))
        schedule.download_bysingername(search_songname,span_number)
        print("complete!")
    else:
        print("Both Empty Error")
except:
    pass
