import pandas as pd

anxman = pd.read_csv('./items_cardkingdom_37.csv')
all = pd.read_csv('./cardIdentifiers.csv')

cardkingdom_scryfall_list = all[['cardKingdomEtchedId', 'cardKingdomFoilId', 'cardKingdomId', 'scryfallId']].values.tolist()

import math 
cardkingdom_scryfall = {}
for _ in cardkingdom_scryfall_list:
    if not math.isnan(_[0]):
        cardkingdom_scryfall[int(_[0])] =_[-1] 
    if not math.isnan(_[1]):
        cardkingdom_scryfall[int(_[1])] =_[-1]  
    if not math.isnan(_[2]):
        cardkingdom_scryfall[int(_[2])] =_[-1]  

api_url = 'https://api.scryfall.com/cards/'
anx_card = list(set(anxman['cardkingdom_id'].values.tolist()))

scryfallids = []
_anx_card = []
for _ in anx_card:
    try:
        scryfallids.append(api_url + str(cardkingdom_scryfall[_])) 
        _anx_card.append(_)
    except:
        continue

print(len(scryfallids))

import requests

with open('output.txt', 'a') as file:
    for url in scryfallids[16803:]:
        response = requests.get(url)
        file.write(str(response.json()['finishes']) + '\n')