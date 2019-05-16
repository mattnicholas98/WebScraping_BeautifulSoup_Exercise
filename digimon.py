import requests
from bs4 import BeautifulSoup
import csv

# url buat digimon
url = 'https://wikimon.net/Visual_List_of_Digimon'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

# initiate list buat nama and gambar digimon
dataDigimon = []

# buat ambil data dri websitenya dan di append ke list
images = y.find_all('img')
for i in images:
    dataDigimon.append({
        'nama' : i.get('alt'),
        'gambar' : 'https://wikimon.net' + i.get('src')
    })

# buat taro di CSV file
with open('digimon.csv', 'w', newline='', encoding='utf-8') as digidata:
    header = ['nama', 'gambar']
    writer = csv.DictWriter(digidata, fieldnames=header)
    writer.writeheader()
    for z in range(len(dataDigimon)-2):     # '-2' in order to remove the last 2 redundant data
        writer.writerow(dataDigimon[z])


# insert data ke mySQL
import mysql.connector

# buat connect ke mysqlnya yang databasenya 'digimon'
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'Matthew',
    password = 'Matthew1998',
    database = 'digimon'
)

cursor = mydb.cursor()

for i in range(len(dataDigimon)-2):
    nama = dataDigimon[i]['nama']
    gambar = dataDigimon[i]['gambar']
    cursor.execute('insert into digimon (nama, gambar) values (%s, %s)', (nama, gambar))    # initiate code buat suruh SQL to do that task
    mydb.commit()   # commit ke SQL