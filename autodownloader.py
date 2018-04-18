import urllib3
import wget 
import sys
from pytube import YouTube

print ("1.Download text or pdf or html files :\n2.Download video from youtube :")
select = int(input("Enter Your choice :"))

if select == 1:
    url = input("Enter your URL to download mp3,pdf :")
   #download_path = input("Enter your Download path :")
    wget.download(url)
    #exec(download_path)
elif select == 2:  
    url1 = input("Enter your URL for video :")
    YouTube(url1).streams.first().download()
    yt = YouTube(url1)
    yt.streams



