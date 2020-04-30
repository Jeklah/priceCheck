import click
import requests
from requests.structures import CaseInsensitiveDict

def get_appraisal():
    url = 'https://www.evepraisal.com/appraisal'
    payload = {
        'raw_textarea': 'Tritanium 1',
        'market': 'jita',
    }
    req = requests.post(url, params=payload)
    appraisal_id = req.headers['X-Appraisal-Id']
    appraisal_url = 'https://www.evepraisal.com/a/{}.json'.format(appraisal_id)
    result = requests.get(appraisal_url).json()


    ## Notes and code that will help
    #
    #convert = str(result).replace('\'', '"')
    #
    # THESE ARE NOT BUY PRICES THEY ARE ALL. CHANGE.

    result['items'][0]['prices']
    tritName = result['items'][0]['name']
    quantity = result['items'][0]['quantity']
    prices = result['items'][0]['prices']['all']
    currAvg = result['items'][0]['prices']['all']['median']
    minPrice = result['items'][0]['prices']['all']['min']
    orderCount = result['items'][0]['prices']['all']['order_count']

    return(result)

def main():
    ret = get_appraisal()
    print(ret)

if __name__ == "__main__":
    main()


