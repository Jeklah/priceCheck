#!/usr/bin/env python3
# Price Check CLI tool for Eve Online
#
# This was a tool aimed at helping people estimate the costs of building
# a ship without the use of complicated spreadsheets that seem
# to break regularly, aren't easy to maintain and hard to use/understand.
#
# But it has ended up being a price check tool!
# Please enjoy and do ask if you have any ideas for new featurs.
#
# This tool aims to solve all of that by being easy to use, maintain and
# easily expandable.
#
# Author: Jeklah
# Date: 10/05/2020

import sys
import click
import requests
import json
from eveConsts import (ship_list,
                       market_list,
                       capital_parts_list,
                       ship_part_counts,
                       ore_list,
                       part_index,
                       pt_index,
                       count_index,
                       min_price)

ship_parts = []      # Initialising the list.


def welcome_msg() -> None:
    """
    Welcome message to be run on first call.

    :return str:
    """
    # os.system('clear')
    welcome = ' ' * 13 + 'Hello and Welcome to Jeklah\'s Ship Cost Calculator'
    click.echo((welcome) + '\n')
    presufix = '*** DISCLAIMER ***'
    disclaim = f'{presufix}This tool assumes 10/20 research on bps.{presufix}'
    click.echo(disclaim)


def choose_market() -> str:
    """
    Provides menu for the user to pick which
    market he would like to get prices from.

    :return str:
    """
    for mrkt in market_list:
        market_menu = f'Ξ {str(market_list.index(mrkt))} {mrkt.capitalize()}\n'
        click.echo(market_menu)
    mrkt_nums = click.IntRange(0, len(market_list))
    market_choice = click.prompt('Please Choose a Market: ', type=mrkt_nums)
    while market_choice < 0 or market_choice > 4:
        click.echo('Please choose a number between 0 and 4.')
        market_choice = click.prompt(
            'Please Choose a Market: ', type=mrkt_nums)
    market_name = market_list[int(market_choice)]
    click.echo(f'You chose {market_name.capitalize()}')
    # time.sleep(1.5)
    return market_name


def choose_ship() -> str:
    """
    Provides menu for the user to choose which ship
    (out of the limited selection thats been implemented)
    to work out the cost of.

    :return str:
    """
    # os.system('clear')
    click.echo('                              Ship Choice')
    click.echo('                 Please choose which ship you would like')
    for ship in ship_list:
        click.echo(f'Ξ {str(ship_list.index(ship))} {ship}' + '\n')
    ship_nbrs = (click.IntRange(0, len(ship_list)))
    choose_ship = 'Choose which ship you would like to calculate costs for: '
    ship_num = click.prompt(choose_ship, type=ship_nbrs)
    click.echo(
        f'You chose the following ship: {ship_list[int(ship_num)]}' + '\n')

    return ship_list[int(ship_num)]


def get_appraisal(item_name: str, market_name: str) -> list:
    """
    This function is how prices are gotten from Eve Online

    :param item_name str:
    :param market_name str:

    :return list:
    """
    # new url for update evepraisal api
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url = 'https://www.evepraisal.com/appraisal/structured.json'
    # new payload for updated evepraisal api
    payload = '{"market_name":"' + market_name + \
              '","items": [{"name": "' + item_name + '", "quantity": 1}]}'
    req = requests.post(url, headers=headers, data=payload)
    json_result = json.loads(req.content)
    appraisal = json_result['appraisal']

    item_name = appraisal['items'][0]['name']
    curr_avg = appraisal['items'][0]['prices']['sell']['avg']
    min_price = appraisal['items'][0]['prices']['sell']['min']
    max_price = appraisal['items'][0]['prices']['sell']['max']

    return [item_name, curr_avg, min_price, max_price]


def item_check(item: str) -> None:
    """
    Function to check item exists.

    :param str:
    """
    try:
        get_appraisal(item, 'jita')
    except KeyError:
        click.echo('Error: Can\'t find item. Please check spelling.')
        sys.exit()


def market_check(market: str) -> None:
    """
    Function to check that the market exists.

    :param str:

    :return list:
    """
    try:
        get_appraisal('Tritanium', market)
    except KeyError:
        click.echo('Error: Can\'t find market. Please check spelling.')
        sys.exit()


def check_both(single: str, market: str) -> None:
    """
    Function to check both that item and market
    exist.
    """
    item_check(single)
    market_check(market)


def ship_parts_cost(ship_name: str, market_name: str) -> str:
    """
    This function collates the parts needed for the ship
    it will then find the price of parts and add them up

    :param str:
    :param str:

    :return str:
    """
    for ship in ship_list:
        if ship_name == ship:
            for x in ship_part_counts[ship_list.index(ship_name)][pt_index][count_index::]:
                if ship_part_counts[ship_list.index(ship_name)][pt_index][0] == 'oreIndex':
                    ship_parts.append(ore_list[int(x)])
                else:
                    ship_parts.append(capital_parts_list[int(x)])
            break

    total = 0
    part_count = dict(
        zip(ship_parts, ship_part_counts[ship_list.index(ship_name)][part_index][count_index::]))
    for item in part_count:
        part_details = get_appraisal(item, market_name)
        part_cost = part_details[3] * float(str(part_count[item]))
        part_cost = round(part_cost, 2)
        total += part_cost
        part_max = f'costs {round(part_details[3], 2):,}'
        click.echo(f'{item} {part_max} ISK at {market_name.capitalize()}')
        click.echo(f'-{item} x {part_count[item]} costs: {part_cost:,} ISK')
        part_max = 'costs {:,}'.format(round(part_details[3], 2))
        click.echo(f'{item} {part_max}' +
                   f' ISK at {market_name.capitalize()}')
        click.echo(
            f'-{item} x {part_count[item]} costs: ' + '{:,}'.format(part_cost) + ' isk')

    total = round(total, 2)
    # click.echo(part_count)
    click.echo(f'Total cost of parts = {total:,} ISK')


@click.command()
@click.option('--compare', '-c', help='Compare the prices of an item at all trading hubs.', type=str)
@click.option('--single', '-s', help='Find out price of a single item. Works with any item!', type=str)
@click.option('--market', '-m', help='The market you would like to use', type=str)
@click.option('--stats', '-st', help='Find out statistics for an item at all markets.', type=str)
def main(single, market, compare, stats):
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
        for mrkt in market_list:
            part_details = get_appraisal(compare, mrkt)
            cost = round(part_details[min_price], 2)
            click.echo(
                f'{compare.capitalize()} costs {cost:,.2f} ISK at {mrkt.capitalize()}'
            )
    elif stats:
        item_check(stats)
        for mrkt in market_list:
            item_details = get_appraisal(stats, mrkt)
            min_cost = round(item_details[min_price], 2)
            avg_cost = round(item_details[1], 2)
            max_cost = round(item_details[3], 2)
            click.echo(
                f'Statistics for {mrkt.capitalize()}: '
            )
            click.echo(
                f'{stats.capitalize()} average cost is {avg_cost:,.2f} ISK.'
            )
            click.echo(
                f'{stats.capitalize()} min price is {min_cost:,.2f} ISK.'
            )
            click.echo(
                f'{stats.capitalize()} max price is {max_cost:,.2f} ISK.\n'
            )

    elif market and not single:
        market_check(market)
        ship_name = choose_ship()
        ship_parts_cost(ship_name, market)
    elif single and not market:
        item_check(single)
        market_name = choose_market()
        part_details = get_appraisal(single, market_name)
        cost = round(part_details[3], 2)
        click.echo(
            f'{single.capitalize()} costs {cost:,.2f} ISK at {market_name.capitalize()}'
        )
    elif single:
        check_both(single, market)
        part_details = get_appraisal(single.lower(), market)
        cost = round(part_details[3], 2)
        click.echo(
            f'{single.capitalize()} costs {cost:,.2f} ISK at {market.capitalize()}'
        )
    else:
        ship_name = choose_ship()
        market_name = choose_market()
        ship_parts_cost(ship_name, market_name)


if __name__ == "__main__":
    main()
