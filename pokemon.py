import requests
from bs4 import BeautifulSoup
import csv

url = 'https://pokemondb.net/pokedex/national'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

# both ID and name ada di dalem class='infocard-lg-data text-muted'
data = y.find_all('span', class_='infocard-lg-data text-muted')

# bkin empty list buat data pokemon
dataPokemon = []
for i in data:
    idPoke = i.find('small').text
    namaPoke = i.find('a').text
    dataPokemon.append({
        'id' : idPoke,
        'nama' : namaPoke
    })

# print(dataPokemon)

# masukin data"nya ke format CSV
with open('pokemon.csv', 'w', newline='', encoding='utf-8') as pokedata:
    header = ['id', 'nama']
    writer = csv.DictWriter(pokedata, fieldnames=header)
    writer.writeheader()
    for i in range(len(dataPokemon)):
        writer.writerow(dataPokemon[i])