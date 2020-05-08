import requests
from eveConsts import shipList, marketList, capitalPartsList, oreList, shipPartCounts, pcIndex
import os

partDetails = []

def welcome():
    print('             Hello and Welcome to Jeklah\'s Ship Cost Calculator')
    print('             Please choose which market you would like to use: ' + '\n')
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
    print('You chose ' + marketName.capitalize() + '\n')

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
    print('You chose the following ship: ' + shipChoice)

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
    shipParts = []

    if shipName =='Orca':
        for x in shipPartCounts[shipList.index(shipName)][pcIndex][pcIndex::]:
            shipParts.append(capitalPartsList[int(x)])
    elif shipName == 'Obelisk':
        for x in shipPartCounts[shipList.index(shipName)][pcIndex][pcIndex::]:
            shipParts.append(capitalPartsList[int(x)])
    elif shipName == 'Venture':
        for x in shipPartCounts[shipList.index(shipName)][pcIndex][pcIndex::]:
            shipParts.append(oreList[int(x)])

    partCount = dict(zip(shipParts, shipPartCounts[shipList.index(shipName)][2][pcIndex::]))
    total = 0
    for item in partCount:
        partDetails = get_appraisal(item, marketName)
        partCost = partDetails[pcIndex] * float(str(partCount[item]))
        partCost = round(partCost, 2)
        total += partCost
        print(item + ' costs ' + '{:,}'.format(round(partDetails[pcIndex], 2)) + ' ISK at ' + marketName.capitalize())
        print('- ' + item + ' x' + partCount[item] + ' costs: ' + '{:,}'.format(partCost) + ' ISK' + '\n')

    total = round(total, 2)
    print('Total cost of parts = ' + '{:,}'.format(total) + ' ISK')

def main():
    welcome()
    marketName = choose_market()
    shipName = choose_ship()
    ship_parts_cost(shipName, marketName)

if __name__ == "__main__":
    main()

