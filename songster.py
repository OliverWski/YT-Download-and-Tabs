def tab(band, song, service, browser):
    
    import time
    import pdfkit
    from AppOpener import run
    from selenium.webdriver.common.by import By
    
    #Search Tab
    browser.get("https://www.songsterr.com/")
    browser.find_element('xpath', '//*[@id="sticky-list-header"]/div[1]/div/input').send_keys(band," ",song)
    time.sleep(1)
    songster = browser.find_elements(By.CLASS_NAME, "B0cew")
    time.sleep(1)
    
    for music_songster in songster:
        music_songster.text
        print("Finding the song")
    
        if song in music_songster.text:
            print(song + "Finded!")
            music_songster.click()
        break
    
    ##If you have songster subscription, choose your path
    
    pdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    url = browser.current_url
    config = pdfkit.configuration(wkhtmltopdf=pdf_path)
    pdfkit.from_url(url, output_path= str(song + ".pdf"), configuration=config)
    
    #Digital Audio Workstation

    run('reaper x')
    
