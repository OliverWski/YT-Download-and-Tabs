## Author: Oliver Rospendowski
## Date: 16/10/2022
## This simple code, download a song, search for the tab to study, create a pdf file, if you have Songster subscription and open reaper DAW. 
## Also if you just wanna download a song, you can simples type "Yes", and paste your YT link.

##Need to install: https://wkhtmltopdf.org/downloads.html - https://www.reaper.fm/download.php

import warnings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from download import music_download
from songster import tab
from song import just_song

if __name__ == '__main__':
    
    #Download just a song
    download = str(input("Do you just wanna download a song?"))
    
    if download == "Yes":
        link = str(input("YT link here: "))
        just_song(link)
        
    else:
        
        #Band and Song
        band = str(input("Choose a Band: "))
        song = str(input("Choose a Song: "))
        
        service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
        
        music_download(band, song, service, browser)
        
        tab(band, song, service, browser)
    
    
    
