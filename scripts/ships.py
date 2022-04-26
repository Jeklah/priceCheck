#!/usr/bin/env python3
# Ship Cost Calculator CLI tool for Eve Online
#
# This is a tool aimed at helping people estimate the costs of building
# a ship without the use of complicated spreadsheets that seem
# to break regularly, aren't easy to maintain and hard to use/understand.
#
# This tool aims to solve all of that by being easy to use, maintain and
# easily expandable.
#
# Author: Arthur Bowers/Jeklah
# Date: 10/05/2020

import click
import requests
from eveConsts import (shipList,
                       marketList,
                       capitalPartsList,
                       oreList,
                       partIndex,
                       ptIndex,
                       countIndex,
                       minPrice)

shipParts = []      # Initialising the list.


def welcome_msg():
    # os.system('clear')
    welcome = ' '*13 + 'Hello and Welcome to Jeklah\'s Ship Cost Calculator'
    click.echo((welcome) + '\n')
    presufix = '*** DISCLAIMER ***'
    disclaim = f'{presufix}This tool assumes 10/20 research on bps.{presufix}'
    click.echo(disclaim)


def choose_market():
    for mrkt in marketList:
        market_menu = f'Ξ {str(marketList.index(mrkt))} {mrkt.capitalize()}\n'
        click.echo(market_menu)
    mrkt_nums = click.IntRange(0, len(marketList))
    marketChoice = click.prompt('Please Choose a Market: ', type=mrkt_nums)
    marketName = marketList[int(marketChoice)]
    click.echo(f'You chose {marketName.capitalize()}')
    # time.sleep(1.5)
    return(marketName)


def choose_ship():
    # os.system('clear')
    click.echo('                              Ship Choice')
    click.echo('                 Please choose which ship you would like')
    for ship in shipList:
        click.echo(f'Ξ {str(shipList.index(ship))} {ship}' + '\n')
    shipNbrs = (click.IntRange(0, len(shipList)))
    chooseShip = 'Choose which ship you would like to calculate costs for: '
    shipNum = click.prompt(chooseShip, type=shipNbrs)
    shipChoice = shipList[int(shipNum)]
    click.echo(f'You chose the following ship: {shipChoice}' + '\n')

    return(shipChoice)


def get_appraisal(itemName, marketName):
    # new url for update evepraisal api
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'https://www.evepraisal.com/appraisal/structured.json'
    # new payload for updated evepraisal api
    payload = '{"market_name":"' + marketName + '","items": [{"name": "' + itemName + '", "quantity": 1}]}'
    # after this point still needs updating.
    # see ipython history for details.
    req = requests.post(url, headers=headers, data=payload)
    click.echo(payload)
    click.echo(req)
    click.echo(req.content) #appraisal_url = f'https://www.evepraisal.com/a/{appraisal_id}.json' #result = requests.get(appraisal_url).json()

    #itemName = result['items'][0]['name']
    #currAvg = result['items'][0]['prices']['sell']['avg']
    #minPrice = result['items'][0]['prices']['sell']['min']
    #maxPrice = result['items'][0]['prices']['sell']['max']

    #return [itemName, currAvg, minPrice, maxPrice]


def item_check(item):
    try:
        get_appraisal(item, 'jita')
    except KeyError:
        click.echo('Error: Can\'t find item. Please check spelling.')
        exit()


def market_check(market):
    try:
        get_appraisal('Tritanium', market)
    except KeyError:
        click.echo('Error: Can\'t find market. Please check spelling.')
        exit()


def check_both(single, market):
    item_check(single)
    market_check(market)


# def ship_parts_cost(shipName, marketName):
#     isk = ' ISK' + '\n'
#     prtTotals = materials[shipList.index(shipName)][ptIndex][countIndex::]
#     cost = (materials[shipList.index(shipName)][ptIndex][0] == 'oreIndex')
#     for ship in shipList:
#         if shipName is ship:
#             for x in prtTotals:
#                 if cost:
#                     shipParts.append(oreList[int(x)])
#                 else:
#                     shipParts.append(capitalPartsList[int(x)])
#             break
# 
#     total = 0
#     partCount = materials[shipList.index(shipName)][partIndex][countIndex::]
#     shipPartCount = dict(zip(shipParts, partCount))
#     for item in shipPartCount:
#         partDetails = get_appraisal(item, marketName)
#         partCost = partDetails[maxPrice] * float(str(shipPartCount[item]))
#         partCost = round(partCost, 2)
#         total += partCost
#         partMax = 'costs {:,}'.format(round(partDetails[maxPrice], 2))
#         click.echo(f'{item} {partMax}' + 'f ISK at {marketName.capitalize()}')
#         click.echo(f'-{item}x{shipPartCount[item]} costs: ' + '{:,}'.format(partCost) + isk)
# 
#     total = round(total, 2)
#     click.echo('Total cost of parts = ' + '{:,}'.format(total) + ' ISK')


@click.command()
@click.option('--compare', '-c', help='Compare the prices of an item at all trading hubs.', type=str)
@click.option('--single', '-s', help='Find out price of a single item. Works with any item!', type=str)
@click.option('--market', '-m', help='The market you would like to use', type=str )
def main(single, market, compare):
    """
    A ship cost calulator tool for Eve Online. This will query the chosen market
    for the prices of the cost of the parts or minerals it takes to build your chosen
    ship. Note: It assumes that the blueprint of the ship you're making is fully researched
    ship.\n
    Note: It assumes that the blueprint of the ship you're making is fully researched
    to 10/20. This could be added as an extra feature if there is demand for it.

    I've added 3 new options.

    These options can be combined for a quick price check at a market.
    If you're using the single item option and the item has spaces in, please contain
    it within single quotes.
    """
    welcome_msg()

    if compare:
        item_check(compare)
        for mrkt in marketList:
            partDetails = get_appraisal(compare, mrkt)
            cost = round(partDetails[minPrice], 2)
            click.echo(compare.capitalize() + ' costs ' + '{:,}'.format(cost) + ' ISK at ' + mrkt.capitalize())
    elif market and not single:
        market_check(market)
        shipName = choose_ship()
        ship_parts_cost(shipName, market)
    elif single and not market:
        item_check(single)
        marketName = choose_market()
        partDetails = get_appraisal(single, marketName)
        cost = round(partDetails[maxPrice], 2)
        click.echo(single.capitalize() + ' costs + ' + '{:,}'.format(cost) + 'ISK at ' + marketName.capitalize())
    elif single and market:
        check_both(single, market)
        partDetails = get_appraisal(single.lower(), market)
        cost = round(partDetails[maxPrice], 2)
        click.echo(single.capitalize() + ' costs ' + '{:,}'.format(cost) + ' ISK at ' + market.capitalize())
    else:
        shipName = choose_ship()
        marketName = choose_market()
        get_appraisal(shipName, marketName)


if __name__ == "__main__":
    main()
