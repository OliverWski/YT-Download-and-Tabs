
def just_song(link):
    
    from pytube import YouTube    

    print("Downloading...")
    link_music_download = str(link)
    link = link_music_download
    yt = YouTube(link)
    yt.streams.filter(only_audio=True)
    stream = yt.streams.get_by_itag(251)
    stream.download()
    print("Downloaded")