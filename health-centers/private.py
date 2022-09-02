import urllib.request
from bs4 import BeautifulSoup
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

file = open("./csv/private-health-centers.csv", "w", newline="")
writer = csv.writer(file)
page_url = "https://pcpndt.karnataka.gov.in/PvtGovtCentresHomepage.aspx?unitid=jJOtHsRVwYECOhoiBc69dA%3d%3d&role=Tg3R3dzL5d8qh2W0SyphdQ%3d%3d&DistWiseCount=BOII5FUynjpl5RZJJ8nW1g%3d%3d&PvtGovt=nBg%2boK7HWWeZVo4G1oAzng%3d%3d"

request = urllib.request.urlopen(page_url).read()
soup = BeautifulSoup(request, "lxml")
tbody = soup('table')[1].find_all('tr')
for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    print(cols)
    writer.writerow(cols)
