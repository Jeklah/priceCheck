#!/usr/bin/env python3
# Ship Cost Calculator CLI tool for Eve Online
#
# This is a tool aimed at helping people estimate the costs of building a ship without
# the use of complicated spreadsheets that seem to break regularly, aren't easy to maintain and
# hard to use/understand.
#
# This tool aims to solve all of that by being easy to use, maintain and easily expandable.
#
# Author: Arthur Bowers/Jeklah
# Date: 10/05/2020

import click
import requests
import time
import os
from eveConsts import shipList, marketList, capitalPartsList, oreList, shipPartCounts, partIndex, ptIndex, countIndex

shipParts = []      # Initialising the list.

#@click.command()
def welcome():
    # os.system('clear')
    click.echo('             Hello and Welcome to Jeklah\'s Ship Cost Calculator' + '\n')
    click.echo('*** DISCLAIMER *** This tool assumes 10/20 research on bps...for now. *** DISCLAIMER ***')

#@click.command()
def choose_market():
    for mrkt in marketList:
        click.echo('Ξ ' + str(marketList.index(mrkt)) + ' ' + mrkt.capitalize() + '\n')
    marketChoice = click.prompt('Please Choose a Market: ', type=click.IntRange(0, len(marketList)))
    marketName = marketList[int(marketChoice)]
    click.echo('You chose ' + marketName.capitalize())
    time.sleep(1.5)

    return(marketName)
#@click.command()
def choose_ship():
    #os.system('clear')
    click.echo('                              Ship Choice')
    click.echo('                 Please choose which ship you would like')
    for ship in shipList:
        click.echo('Ξ ' + str(shipList.index(ship)) + ' ' + ship + '\n')
    shipNum = click.prompt('Choose which ship you would like to calculate costs for: ', type=click.IntRange(0, len(shipList)))
    shipChoice = shipList[int(shipNum)]
    click.echo('You chose the following ship: ' + shipChoice + '\n')

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
        click.echo(item + ' costs ' + '{:,}'.format(round(partDetails[ptIndex], 2)) + ' ISK at ' + marketName.capitalize())
        click.echo('- ' + item + ' x ' + partCount[item] + ' costs: ' + '{:,}'.format(partCost) + ' ISK' + '\n')

    total = round(total, 2)
    click.echo('Total cost of parts = ' + '{:,}'.format(total) + ' ISK')

@click.command()
@click.option('--single', '-s', help='Find out price of one item. See help for more info.', default=False)
@click.option('--market', '-m', help='The market you would like to use', default=False)
def main(single, market):
    """
    A ship cost calulator tool for Eve Online. This will query the chosen market
    for the prices of the cost of the parts or minerals it takes to build your chosen
    ship. Note: It assumes that the blueclick.echo of the ship you're making is fully researched
    to 10/20. This could be added as an extra feature if there is demand for it.

    If you're going to use the single item appraisal and the item has spaces in, please contain
    it within single quotes.
    """
    welcome()
    if single:
        if market:
            try:
                marketName = market
            except ValueError:
                click.echo('Please enter a market selection by number.')
            else:
                partDetails = get_appraisal(single.lower(), marketName)
                cost = round(partDetails[1], 2)
                click.echo(single.capitalize() + ' costs ' + '{:,}'.format(cost) + ' ISK at ' + marketName.capitalize())
        else:
            partDetails = get_appraisal(single.lower(), marketName)
            cost = round(partDetails[1], 2)# To-DO change this index to currAverage.
            click.echo(single.capitalize() + ' costs ' + '{:,}'.format(cost) + ' ISK at ' + marketName.capitalize())
    else:
        marketName = choose_market()
        shipName = choose_ship()
        ship_parts_cost(shipName, marketName)

if __name__ == "__main__":
    main()
