import requests
import csv
from bs4 import BeautifulSoup
page = requests.get('https://en.wikipedia.org/wiki/List_of_brown_dwarfs')
headers = ['Star_name', 'Distance', 'Mass', 'Radius']
soup = BeautifulSoup(page.text, 'html.parser')
tables = soup.find_all('table')
tr_tags =  tables[5].find_all('tr')
stars_data = []
temp_list = []

for tr in tr_tags:
    td_tags = tr.find_all('td')
    row = [i.text.strip() for i in td_tags]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    name = temp_list[i][0]
    distance = temp_list[i][5]
    mass = temp_list[i][7]
    radius = temp_list[i][8]
    stars_data.append((name, distance, mass, radius))

with open('result.csv', 'w', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)