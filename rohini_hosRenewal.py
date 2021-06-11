import urllib.request
from bs4 import BeautifulSoup, element
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

pages = list(range(1, 8))
for page in pages:
    file = open(f'rohini_hosRenewal/page_{page}.csv', "w", newline="")
    writer = csv.writer(file)
    print(page)
    page_url = f'https://rohini.iib.gov.in/HosRenewal/index/page:{page}?status=p&search=Search'

    request = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(request, 'lxml')
    tbody = soup('table')[0].find_all('tr')
    for row in tbody:
        cols = row.findChildren(recursive=False)
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)