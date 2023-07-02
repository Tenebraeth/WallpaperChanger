from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import ctypes
import os.path
import time

def WallpaperChangee(img_text):
    #variables
    ua = UserAgent()
    img_text = '/search/' + img_text
    link = 'https://zastavok.net'
    img_path = os.path.abspath('pictures\image.png')

    #find_pictures
    response = requests.get(link + img_text, headers={'user-agent':f'{ua.random}'}).text
    soup = BeautifulSoup(response, 'html.parser')
    all_image = soup.findAll('div', class_='short_prev')

    #download
    for image in all_image:
        image_link = image.find('a').get('href')
        download_storage = requests.get(link + image_link, headers={'user-agent':f'{ua.random}'}).text

        download_soup = BeautifulSoup(download_storage, 'html.parser')
        download_block = download_soup.find('div', class_='block_down')

        result_link = download_block.find('a').get('href')
        image_bytes = requests.get(f'{link}{result_link}').content

        with open('pictures/image.png', 'wb') as file:
            file.write((image_bytes))

        #set_wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)
        time.sleep(4)