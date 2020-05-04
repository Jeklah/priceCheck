# import click  to be implemented at later date
import requests

partDetails = []
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
                'Capital Corporate Hangar Bay',
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
    print('Please choose which market you would like to use: ' + '\n')
    for mrkt in marketList:
        print('Ξ ' + str(marketList.index(mrkt)) + ' ' + mrkt.capitalize() + '\n')

def choose_market():
    marketChoice = input('Your choice by number: ')
    market = marketList[int(marketChoice)]
    print('You chose ' + market.capitalize() + '\n')

    return(market)

def get_appraisal(item, market):
    url = 'https://www.evepraisal.com/appraisal'
    payload = {
        'raw_textarea': item + ' 1',
        'market': market,
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

def ship_parts_cost(market):
    partCount = dict(zip(partsList, shipPartCounts['Orca']))
    total = 0

    for item in partCount:
        partDetails = get_appraisal(item, market)
        partCost = partDetails[1] * float(partCount[item])
        partCost = round(partCost, 2)
        total += partCost
        print(item + ' costs ' + '{:,}'.format(round(partDetails[1], 2)) + ' ISK at ' + market.capitalize())
        print('- ' + item + ' x' + partCount[item] + ' costs: ' + '{:,}'.format(partCost) + ' ISK' + '\n')

    total = round(total, 2)
    print('Total cost of parts = ' + '{:,}'.format(total) + ' ISK')

def main():
    welcome()
    market = choose_market()
    ship_parts_cost(market)

if __name__ == "__main__":
    main()

