import urllib.request
from bs4 import BeautifulSoup, element
import ssl
import csv

ssl._create_default_https_context = ssl._create_unverified_context

states = {
    'ladakh': 'LK',
    'jammu&kashmir': 'JK',
    'himanchal': 'HP',
    'punjab': 'PB',
    'uttarakhand': 'UK',
    'uttarpradesh': 'UP',
    'haryana': 'HR',
    'delhi': 'DL',
    'bihar': 'BR',
    'sikkim': 'SK',
    'assam': 'AS',
    'arunanchal': 'AP',
    'nagaland': 'NG',
    'Andhra Pradesh': 'AP',
    'Chhattisgarh': 'CG',
    'Goa': 'GA',
    'Gujarat': 'GJ',
    'Jharkhand': 'JH',
    'Karnataka': 'KA',
    'Kerala': 'KL',
    'Madhya Pradesh': 'MP',
    'Maharashtra': 'MH',
    'Manipur': 'MN',
    'Meghalaya': 'ML',
    'Mizoram': 'MZ',
    'Nagaland': 'NL',
    'Odisha': 'OD',
    'Rajasthan': 'RJ',
    'Tamil Nadu': 'TN',
    'Tripura': 'TR',
    'West Bengal': 'WB',
    'Telangana': 'TS',
    'Puduchery': 'PN',
    'Chandigarh': 'CH',
    'Dadra and Nagar Haveli': 'DN',
    'Daman and Diu': 'DD',
    'Lakshadweep': 'LD',
}

state_names = list(states.keys())
for state in state_names:
    file = open(f'csv/states/{state}.csv', "w", newline="")
    writer = csv.writer(file)
    page_url = f'https://elora.aerb.gov.in/ELORA/graphDataListByStateSummary.htm?state={states[state]}'

    request = urllib.request.urlopen(page_url).read()
    soup = BeautifulSoup(request, 'lxml')
    tbody = soup('table', {"id": "displayDataTblSummary"})[0].find_all('tr')
    print(f'scrapping: {state}')

    for row in tbody:
        cols = row.findChildren(recursive=False)
        cols = [ele.text.strip() for ele in cols]
        writer.writerow(cols)