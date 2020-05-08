# import click  to be implemented at later date
import requests
import eveConsts
import os

partDetails = []

def welcome():
    print('Hello and Welcome to Jeklah\'s Ship Cost Calculator')
    print('Please choose which market you would like to use: ' + '\n')
    for mrkt in eveConsts.marketList:
        print('Ξ ' + str(eveConsts.marketList.index(mrkt)) + ' ' + mrkt.capitalize() + '\n')

def choose_market():
    marketChoice = input('Choose market by number: ')
    marketName = eveConsts.marketList[int(marketChoice)]
    print('You chose ' + marketName.capitalize() + '\n')

    return(marketName)

def choose_ship():
    os.system('clear')
    for ship in eveConsts.shipList:
        print('Ξ ' + str(eveConsts.shipList.index(ship)) + ' ' + ship + '\n')
    shipNum = input('Choose which ship you would like to calculate costs for: ')
    shipChoice = eveConsts.shipList[int(shipNum)]
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
        for x in range(1,len(eveConsts.capitalPartsList)):
            shipParts.append(eveConsts.capitalPartsList[x])
    elif shipName == 'Obelisk':
        for x in range(1, len(eveConsts.shipPartCounts[1][2])):
            shipParts.append(eveConsts.capitalPartsList[x])
    else:
        for x in range(len(eveConsts.oreList)):
            shipParts.append(eveConsts.oreList[x])

    partCount = dict(zip(shipParts, eveConsts.shipPartCounts[0][2][1::]))
    total = 0
    print(partCount)
    for item in partCount:
        partDetails = get_appraisal(item, marketName)
        partCost = partDetails[1] * float(str(partCount[item]))
        partCost = round(partCost, 2)
        total += partCost
        print(item + ' costs ' + '{:,}'.format(round(partDetails[1], 2)) + ' ISK at ' + marketName.capitalize())
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

