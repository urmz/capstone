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

from bs4 import BeautifulSoup
import requests

#Job websites
page_link = 'https://www.alexa.com/topsites/category/Business/Employment/Job_Search'
page_response = requests.get(page_link, timeout=5)
page_contentz = BeautifulSoup(page_response.content, "html.parser")
job_web_list = []
for i in range(12,137):
    site = page_contentz.find_all("p")[i].text
    if i == 12 or (i-12)%5 == 0 :
        job_web_list.append(site.encode("ascii")[1:-1])

#US websites
page_link = 'https://www.alexa.com/topsites/countries/US'
page_response = requests.get(page_link, timeout=5)
page_contentz = BeautifulSoup(page_response.content, "html.parser")
us_web_list = []
for i in range(11,137):
    site = page_contentz.find_all("p")[i].text
    if i == 11 or (i-11)%5 == 0 :
        us_web_list.append(site.encode("ascii")[1:-1])

#AfAm Websites
page_link = 'https://www.alexa.com/topsites/category/Society/Ethnicity/African/African-American'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
afam_web_list = []
for i in range(12,137):
    site = page_content.find_all("p")[i].text
    if i == 12 or (i-12)%5 == 0 :
        afam_web_list.append(site.encode("ascii")[1:-1])
        #web_list.append(site[1:-1])
        
        
# sites = [row.strip() for row in open(url_path, 'r')]
n_total = 2
n_control = n_total/2
n_treat = n_total/2 

#treatment group
for x in range(n_treat):
    driver = Chrome('/Users/urmilajanardan/Desktop/chromedriver')
    #create web browser
    for y in afam_web_list:
        driver.get("http://" + y )
        time.sleep(3)
    #drives webpage to all sites in web_list 
    
    for y in job_web_list:
        driver.get("http://" + y )
        time.sleep(3)
    #drives webpage to all sites in web_list 


#control group
for x in range(n_treat):
    driver = Chrome('/Users/urmilajanardan/Desktop/chromedriver')
    #create web browser
    
    for y in us_web_list:
        driver.get("http://" + y )
    #drives webpage to all sites in web_list 
    
    for y in job_web_list:
        driver.get("http://" + y )
    #drives webpage to all sites in web_list
