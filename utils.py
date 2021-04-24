import os
import requests
from bs4 import BeautifulSoup

def clear():
    os.system('cls')

def get_page_soup(page_url):
    resp = requests.get(page_url)
    return BeautifulSoup(str(resp.content), "lxml")