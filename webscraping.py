from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from seleniumrequests import Chrome
import pickle
import json
import requests
import datetime
import pandas as pd
import numpy as np

# Webscraping Tutorial: https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486

from bs4 import BeautifulSoup
import requests
# Here, we're just importing both Beautiful Soup and the Requests library

page_link = 'https://www.alexa.com/topsites/category/Society/Ethnicity/African/African-American'
# this is the url that we've already determined is safe and legal to scrape from.

page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library

page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.

afam_web_list = []
for i in range(12,262):
    site = page_content.find_all("p")[i].text
    if i == 12 or (i-12)%5 == 0 :
        afam_web_list.append(site.encode("ascii")[1:-1])
        #web_list.append(site[1:-1])


#US websites
page_link = 'https://www.alexa.com/topsites/countries/US'
page_response = requests.get(page_link, timeout=5)
page_contentz = BeautifulSoup(page_response.content, "html.parser")
us_web_list = []
for i in range(11,262):
    site = page_contentz.find_all("p")[i].text
    if i == 11 or (i-11)%5 == 0 :
        us_web_list.append(site.encode("ascii")[1:-1])
        
#Job websites
page_link = 'https://www.alexa.com/topsites/category/Business/Employment/Job_Search'
page_response = requests.get(page_link, timeout=5)
page_contentz = BeautifulSoup(page_response.content, "html.parser")
job_web_list = []
for i in range(12,262):
    site = page_contentz.find_all("p")[i].text
    if i == 12 or (i-12)%5 == 0 :
        job_web_list.append(site.encode("ascii")[1:-1])
