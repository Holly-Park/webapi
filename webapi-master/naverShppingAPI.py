import json
import requests 
import os
import sys
import urllib.request
import sqlite3


# client_id = “pbIkSEjwEDmhIVpOTRYj”
# client_secret = “avwHJhQd6D
# encText = urllib.parse.quote("스마트”)
# url = 'https://openapi.naver.com/v1/search/blog?query=' + encText 

url = 'https://openapi.naver.com/v1/search/shop.json?query=스마트&display=10&start=1&sort=sim'
header = {'X-Naver-Client-Id':'pbIkSEjwEDmhIVpOTRYj', 'X-Naver-Client-Secret':'avwHJhQd6D'}

response = requests.get(url, headers = header)
response.status_code
rt_dict = json.loads(response.content)
print(rt_dict.keys())

import pandas as pd
print(pd.DataFrame(rt_dict['items']))



#DB에 저장

