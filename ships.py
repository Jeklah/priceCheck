import click
import requests
from requests.structures import CaseInsensitiveDict

components = []
oreList = [
            'Tritanium',
            'Pyerite',
            'Isogen',
            'Megacyte',
            'Mexallon',
            'Nocxium',
            'Zydrine'
           ]

marketList = [
                'jita',
                'hek',
                'amarr',
                'rens',
                'dodixie'
              ]

partsList = [
                'Capital Capacitor Battery',
                'Capital Cargo Bay',
                'Capital Computer System',
                'Capital Construction Parts',
                'Capital Corporate Hanger Bay',
                'Capital Sensor Cluster',
                'Capital Ship Maintenance Bay'
            ]

shipPartCounts = {
                    'Orca':{
                        '9',
                        '35',
                        '7',
                        '15',
                        '4',
                        '4',
                        '7'
                    }
                 }

def welcome():
    print('Hello and Welcome to Jeklah\'s Ship Cost Calculator')
    print('Please choose which market you would like to use: ')
    for market in marketList:
        print('Ξ ' + marketList.index(market) + ' ' + market + '\n')

def choose_market():
    marketChoice = input('Your choice by number: ')

    return(marketList[marketChoice])

def get_appraisal(item, market):
    url = 'https://www.evepraisal.com/appraisal'
    payload = {
        'raw_textarea': item + ' 1',
        'market': market
    }
    req = requests.post(url, params=payload)
    appraisal_id = req.headers['X-Appraisal-Id']
    appraisal_url = 'https://www.evepraisal.com/a/{}.json'.format(appraisal_id)
    result = requests.get(appraisal_url).json()

    ## Notes and code that will help
    #
    # convert = str(result).replace('\'', '"')
    # result['items'][0]['prices']
    # prices = result['items'][0]['prices']['buy']
    # quantity = result['items'][0]['quantity']

    itemName = result['items'][0]['name']
    currAvg = result['items'][0]['prices']['buy']['avg']
    minPrice = result['items'][0]['prices']['buy']['min']
    maxPrice = result['items'][0]['prices']['buy']['max']

    return(itemName, currAvg, minPrice, maxPrice)

def ship_parts_cost(market):
    partCount = dict(zip(partsList, shipPartCounts['Orca']))
    total = 0

    for part in partCount:
        partDetails = get_appraisal(part, market)
        partCost = partDetails[1] * partCount[part]
        total += partCost
        print('- ' + part + 'x' + partCount[part] + ' costs: ' + partCost + ' ISK')

    print('Total cost of parts = ' + total)

    return(total)


def main():
    welcome()
    market = choose_market()
    ship_parts_cost(market)
    ret = get_appraisal()
    print(ret)

if __name__ == "__main__":
    main()

