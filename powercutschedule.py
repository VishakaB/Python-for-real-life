import datetime
from urllib.request import urlopen

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import certifi
import ssl
import certifi

requests.get('https://google.com', verify=r'C:\Users\visha\PycharmProjects\pythonProject\venv\lib\site-packages\certifi\cacert.pem')
headers0 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
          }
url = 'https://ceb.lk/'

r = requests.get(url, headers =headers0,verify=True)


# Parse HTML file in Beautiful Soup
soup = bs(url, 'html.parser')

# Finding the location of button
btn = soup.find("button", {"id": "Click here"})

print(btn)

# Obtaining the onclick link of button tag
