import requests
import json

from log4py import Logger

Logger.set_level("INFO")
log = Logger.get_logger(__name__)

# COIN_MARKET_API_KEY = '70131ef7-eb12-418f-89fe-5e9564c96379'
COIN_MARKET_API_KEY = '73a77d19-503c-4d07-b368-6f00a71f668c'


def getMarketPrice():
    currentBABYPrice = 0
    currentMILKPrice = 0
    response = requests.get(
        'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
        params={'symbol': 'BABY,MILK'},
        headers={'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': COIN_MARKET_API_KEY},
        timeout=1
    )
    dicts = json.loads(response.text)
    if dicts['status']['error_code'] == 0:
        currentBABYPrice = dicts['data']['BABY']['quote']['USD']['price']
        currentMILKPrice = dicts['data']['MILK']['quote']['USD']['price']
    log.info("BABY : " + str(currentBABYPrice) + " USDT")
    log.info("MILK : " + str(currentMILKPrice) + " USDT")
    return currentBABYPrice, currentMILKPrice


def getMarketList():
    response = requests.get('https://service.thecryptoyou.io/nft/market/list', timeout=1)
    dicts = json.loads(response.text)
    sortedList = []
    if dicts['massage'] == 'Success':
        sortedList = sorted(dicts['data'], key=lambda i: i['createDate'], reverse=True)
    return sortedList


def getLeaderInfo():
    response = requests.post('https://graph.babyswap.info/subgraphs/name/bscmainbabyswap/leaderboard1',
                             timeout=1,
                             headers={
                                 'Accepts': 'application/json',
                                 'Content-Type': 'application/json',
                                 'origin': 'https://thecryptoyou.io'})
    print(response.text)
