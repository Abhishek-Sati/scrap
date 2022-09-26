import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

file = open("../csv/service-agencies.csv", "w", newline="")
writer = csv.writer(file)
page_url = 'https://elora.aerb.gov.in/ELORA/prePopulateGraphData.htm#tabs-6'

request = urllib.request.urlopen(page_url).read()
soup = BeautifulSoup(request, "lxml")

tbody = soup('table')[8].find_all('tr')
for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    print(cols)
    writer.writerow(cols)
