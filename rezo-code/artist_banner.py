""" # for an artist id, return their spotify banner's url
# style="background-image: url("https://i.scdn.co/image/ab67618600001016fffc76a8ae5788d8e8332861");" 


import httpx
from bs4 import BeautifulSoup

SPOTIFY_ARTIST_URL = "https://open.spotify.com/artist/"
# REZO_ARTIST_URL = "https://listen.rezonance.in/artist/"
BANNER_CLASS = "k2I8B0MzXkAJ6_s8okM7"

artist_id = "0GF4shudTAFv8ak9eWdd4Y"
artist_page = httpx.get(f"{SPOTIFY_ARTIST_URL}{artist_id}").text
# print(artist_page)

soup = BeautifulSoup(artist_page, 'html.parser')
banner_url = soup.find_all(class_=BANNER_CLASS)
print(soup)
# print(banner_url) """

############################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SPOTIFY_ARTIST_URL = "https://open.spotify.com/artist/"
# REZO_ARTIST_URL = "https://listen.rezonance.in/artist/"
BANNER_CLASS = "k2I8B0MzXkAJ6_s8okM7"
artist_id = "0GF4shudTAFv8ak9eWdd4Y"

driver = webdriver.Chrome()
artist_page = driver.get(f"{SPOTIFY_ARTIST_URL}{artist_id}")
time.sleep(10)
banner_div = driver.find_element(By.CLASS_NAME, BANNER_CLASS)
banner_url = banner_div.value_of_css_property('background-image').split('"')[1]

print(banner_url)
# driver.quit()