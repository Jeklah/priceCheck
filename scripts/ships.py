# Ship Cost Calculator CLI tool for Eve Online
#
# This is a tool aimed at helping people estimate the costs of building a ship without
# the use of complicated spreadsheets that seem to break regularly, aren't easy to maintain and
# hard to use/understand/
#
# This tool aims to solve all of that by being easy to use, maintain and easily expandable.
#
# Author: Arthur Bowers/Jeklah
# Date: 10/05/2020

import requests
import time
import os
from eveConsts import shipList, marketList, capitalPartsList, oreList, shipPartCounts, partIndex, ptIndex, countIndex

shipParts = []

def welcome():
    print('             Hello and Welcome to Jeklah\'s Ship Cost Calculator')
    print('*** DISCLAIMER *** This tool assumes 10/20 research on bps...for now. *** DISCLAIMER ***')
    print('             Please choose which market you would like to use: ')
    for mrkt in marketList:
        print('Ξ ' + str(marketList.index(mrkt)) + ' ' + mrkt.capitalize() + '\n')

def choose_market():
    while True:
        try:
            marketChoice = int(input('Choose market by number: '))
        except ValueError:
            print('Please enter your choice with numbers, not words.')
            continue
        if marketChoice < 0 or marketChoice > (len(marketList) - 1):   # -1 because python len uses a start index of 1
            print('Please enter a valid number.')
            continue
        else:
            break
    marketName = marketList[int(marketChoice)]
    print('You chose ' + marketName.capitalize())
    time.sleep(1.5)

    return(marketName)

def choose_ship():
    os.system('clear')
    print('             Ship Choice')
    for ship in shipList:
        print('Ξ ' + str(shipList.index(ship)) + ' ' + ship + '\n')
    while True:
        try:
            shipNum = int(input('Choose which ship you would like to calculate costs for: '))
        except ValueError:
            print('Please enter numbers not words. Preferably in range.')
            continue
        if shipNum < 0 or shipNum > (len(shipList) - 1):
            print('Please enter a valid number.')
            continue
        else:
            break

    shipChoice = shipList[int(shipNum)]
    print('You chose the following ship: ' + shipChoice + '\n')

    return(shipChoice)

def get_appraisal(itemName, marketName):
    url = 'https://www.evepraisal.com/appraisal'
    payload = {
        'raw_textarea': itemName + ' 1',
        'market': marketName,
    }

    req = requests.post(url, params=payload)
    appraisal_id  = req.headers['X-Appraisal-Id']
    appraisal_url = 'https://www.evepraisal.com/a/{}.json'.format(appraisal_id)
    result = requests.get(appraisal_url).json()

    itemName = result['items'][0]['name']
    currAvg  = result['items'][0]['prices']['sell']['avg']
    minPrice = result['items'][0]['prices']['sell']['min']
    maxPrice = result['items'][0]['prices']['sell']['max']

    partDetails = [itemName, currAvg, minPrice, maxPrice]

    return(partDetails)

def ship_parts_cost(shipName, marketName):
    for ship in shipList:
        if shipName is ship:
            for x in shipPartCounts[shipList.index(shipName)][ptIndex][countIndex::]:
                if shipPartCounts[shipList.index(shipName)][ptIndex][0] == 'oreIndex':
                    shipParts.append(oreList[int(x)])
                else:
                    shipParts.append(capitalPartsList[int(x)])
            break

    total = 0
    partCount = dict(zip(shipParts, shipPartCounts[shipList.index(shipName)][partIndex][countIndex::]))
    for item in partCount:
        partDetails = get_appraisal(item, marketName)
        partCost = partDetails[ptIndex] * float(str(partCount[item]))
        partCost = round(partCost, 2)
        total += partCost
        print(item + ' costs ' + '{:,}'.format(round(partDetails[ptIndex], 2)) + ' ISK at ' + marketName.capitalize())
        print('- ' + item + ' x ' + partCount[item] + ' costs: ' + '{:,}'.format(partCost) + ' ISK' + '\n')

    total = round(total, 2)
    print('Total cost of parts = ' + '{:,}'.format(total) + ' ISK')

def main():
    welcome()
    marketName = choose_market()
    shipName = choose_ship()
    ship_parts_cost(shipName, marketName)

if __name__ == "__main__":
    main()
