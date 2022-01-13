import logging

import simpleaudio
import logging
import threading
import time
import static_data
import models
import spider
import strategy
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('thecryptoyou')
log_format = "%(asctime)s - %(message)s"
handler = TimedRotatingFileHandler("./logs/market_notice.log", when="midnight", interval=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
# add a suffix which you want
handler.suffix = "%Y%m%d"
# finally add handler to logger
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def play_music():
    wave_obj = simpleaudio.WaveObject.from_wave_file("./15011.wav")
    play_obj = wave_obj.play()
    while True:
        if not (play_obj.is_playing()):
            break


# default price is 2022-01-04 price,usdt
currentBABYPrice = 0.714445
currentMILKPrice = 0.001


def get_price(originPrice):
    integerPrice = originPrice[0:len(originPrice) - 18]
    decimalPrice = originPrice[len(originPrice) - 18:len(originPrice) - 16]
    finalPrice = integerPrice + "." + decimalPrice
    return finalPrice


def getTotalScore(level, totalAttr, mainAttr, subAttr):
    return ((level * 0.05) + 0.5) * mainAttr + ((level * 0.01) + 0.1) * subAttr + (totalAttr * (1 + (0.1 * level)))


def notice(data, baby, babyLevelOnePriceWithUSDT, styPrice, styName):
    play_music()

    totalScore = getTotalScore(baby.level, baby.getTotalAttr(), baby.getMainAttr(), baby.getSubAttr())
    formatTotalScore = '%.2f' % totalScore
    price = get_price(data['price'])
    priceInUSDT = 0
    if data['token'] == 'BABY':
        priceInUSDT = float(price) * currentBABYPrice
    elif data['token'] == 'MILK':
        priceInUSDT = float(price) * currentMILKPrice

    expectPercent = babyLevelOnePriceWithUSDT / styPrice
    formatPriceInUSDt = '%.2f' % priceInUSDT
    formatExpectPercent = '%.2f' % (expectPercent * 100)

    importantStr = "*****"
    importantWeight = int((1 / expectPercent) * 10)
    for i in range(0, importantWeight):
        importantStr += "*****"
    logger.info(
        "\n" + importantStr +
        "\n" + styName +
        "\n Price : " + price + " " + data[
            'token'] + "(" + formatPriceInUSDt + "USDT)" + " " + formatExpectPercent + "%" +
        "\n Baby Name :" + baby.name +
        "\n Baby RARITY :" + baby.rarity +
        "\n Main Attr(" + static_data.ATTRS_MAP[static_data.MAIN_ATTR_MAP[baby.nftIndex]] + ") :" + str(
            baby.getMainAttr()) +
        "\n Sub Attr(" + static_data.ATTRS_MAP[static_data.SUB_ATTR_MAP[baby.nftIndex]] + ") :" + str(
            baby.getSubAttr()) +
        "\n Level : " + str(baby.level) +
        "\n TotalAttr : " + str(baby.getTotalAttr()) +
        "\n TotalScore : " + str(formatTotalScore) +
        "\n ID : " + "https://thecryptoyou.io/market/" + data['nftId'] + "\n")


def isNotice(stgy, baby, babyLevelOnePriceWithUSDT):
    if baby.getMainAttr() >= stgy.mainAttr and baby.getSubAttr() >= stgy.subAttr and baby.getTotalAttr() >= stgy.score:
        if babyLevelOnePriceWithUSDT == 0:
            return False
        if babyLevelOnePriceWithUSDT <= stgy.noticePrice:
            return True
    return False


def check():
    logger.debug("\nMonitor running" +
                 "\nBABY current price(USDT)" + str(currentBABYPrice) +
                 "\nMILK current price(USDT)" + str(currentMILKPrice))
    sortedList = spider.getMarketList()
    for num in range(0, 5):
        data = sortedList[num]
        info = data['info']
        baby = models.Baby(info)
        token = data['token']
        babyPriceWithUSDT = 0
        if token == 'BABY':
            babyPriceWithUSDT = float(get_price(data['price'])) * currentBABYPrice
        elif token == 'MILK':
            babyPriceWithUSDT = float(get_price(data['price'])) * currentMILKPrice
        babyLevelOnePriceWithUSDT = 0
        if baby.level == 5:
            babyLevelOnePriceWithUSDT = babyPriceWithUSDT - (
                    1000 * currentBABYPrice + 220000 * currentMILKPrice)
        elif baby.level == 4:
            babyLevelOnePriceWithUSDT = babyPriceWithUSDT - (220000 * currentMILKPrice)
        elif baby.level == 3:
            babyLevelOnePriceWithUSDT = babyPriceWithUSDT - (70000 * currentMILKPrice)
        elif baby.level == 2:
            babyLevelOnePriceWithUSDT = babyPriceWithUSDT - (20000 * currentMILKPrice)
        elif baby.level == 1:
            babyLevelOnePriceWithUSDT = babyPriceWithUSDT

        for stgy in strategy.strategies:
            if (stgy.babyName != "" and stgy.babyName == baby.name) or (stgy.rarity == baby.rarity):
                if isNotice(stgy, baby, babyLevelOnePriceWithUSDT):
                    notice(data, baby, babyLevelOnePriceWithUSDT, stgy.noticePrice, stgy.name)


def AutoUpdateCurrentPrice():
    global currentBABYPrice
    global currentMILKPrice
    while True:
        try:
            babyP, milkP = spider.getMarketPrice()
            if babyP > 0 and milkP > 0:
                currentBABYPrice = babyP
                currentMILKPrice = milkP
            time.sleep(300)
        except Exception as apiErr:
            logger.debug(apiErr)
            time.sleep(300)


def AutoCheckMarket():
    while True:
        try:
            check()
            time.sleep(3)
        except Exception as e:
            logger.debug(e)


t = threading.Thread(target=AutoUpdateCurrentPrice)
t.start()

tAutoCheckoutMarket = threading.Thread(target=AutoCheckMarket)
tAutoCheckoutMarket.start()
