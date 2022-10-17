def music_download(band, song, service, browser):
    
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver import ActionChains
    from pytube import YouTube
       
    #Chrome Settings
    browser.maximize_window()
    
    #Search Music
    band_search=band.replace(" ","+")
    song_search=song.replace(" ","+")
    music = "https://www.youtube.com/results?search_query="+band_search+"+"+song_search
    browser.get(music)
    list_yt = browser.find_elements(By.CLASS_NAME, "style-scope ytd-video-renderer")
    
    action = ActionChains(browser)
    
    time.sleep(2)
    
    for music_youtube in list_yt:
        print("Seaching...")
        music_youtube.text
        
        if song in music_youtube.text:
            action.double_click(music_youtube).perform()
            print("Finded!")
        break
                   
    #Download the song
    time.sleep(1)
    print("Downloading...")       
    link_music_download = str(browser.current_url)
    time.sleep(1)
    yt = YouTube(link_music_download)
    yt.streams.filter(only_audio=True)
    stream = yt.streams.get_by_itag(251)
    stream.download()
    print("Downloaded")
