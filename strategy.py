import static_data
import models


def newStrategy(name="", babyName="", token="USDT", mainAttr=0, subAttr=0, noticePrice=0, score=0, rarity=""):
    strategy = models.Strategy()
    strategy.name = name
    strategy.babyName = babyName
    strategy.token = token
    strategy.mainAttr = mainAttr
    strategy.subAttr = subAttr
    strategy.noticePrice = noticePrice
    strategy.score = score
    strategy.rarity = rarity
    return strategy


strategies = [
    # ssr 99
    newStrategy(
        name="SSR 99 420+ low price notice",
        mainAttr=99,
        subAttr=61,
        noticePrice=2500,
        score=420,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 99 410+ low price notice",
        mainAttr=99,
        subAttr=61,
        noticePrice=1500,
        score=410,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 99 400+ low price notice",
        mainAttr=99,
        subAttr=61,
        noticePrice=1000,
        score=400,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 99 390+ low price notice",
        mainAttr=99,
        subAttr=61,
        noticePrice=500,
        score=390,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 99 low price notice",
        mainAttr=99,
        subAttr=61,
        noticePrice=300,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 98 420+ low price notice",
        mainAttr=98,
        subAttr=61,
        noticePrice=1000,
        score=420,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 98 410 low price notice",
        mainAttr=98,
        subAttr=61,
        score=410,
        noticePrice=600,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    # ssr 98
    newStrategy(
        name="SSR 98 400 low price notice",
        mainAttr=98,
        subAttr=61,
        score=400,
        noticePrice=500,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 98 390 low price notice",
        mainAttr=98,
        subAttr=61,
        score=390,
        noticePrice=300,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 98 low price notice",
        mainAttr=98,
        subAttr=61,
        noticePrice=200,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    # ssr 97
    newStrategy(
        name="SSR 97 420+ low price notice",
        mainAttr=97,
        subAttr=61,
        noticePrice=1000,
        score=420,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 97 410 low price notice",
        mainAttr=97,
        subAttr=61,
        score=410,
        noticePrice=600,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 97 400 low price notice",
        mainAttr=97,
        subAttr=61,
        score=400,
        noticePrice=500,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 97 390 low price notice",
        mainAttr=97,
        subAttr=61,
        score=390,
        noticePrice=300,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    newStrategy(
        name="SSR 97 low price notice",
        mainAttr=97,
        subAttr=61,
        noticePrice=200,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    # ssr 90
    newStrategy(
        name="SSR 90 low price notice",
        mainAttr=90,
        subAttr=61,
        noticePrice=100,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    # ssr low
    newStrategy(
        name="SSR low price notice",
        mainAttr=10,
        noticePrice=30,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SSR]),
    # sr 99
    newStrategy(
        name="SR 99 340 low price notice",
        mainAttr=99,
        subAttr=61,
        score=340,
        noticePrice=1200,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 330 low price notice",
        mainAttr=99,
        subAttr=61,
        score=330,
        noticePrice=500,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 320 low price notice",
        mainAttr=99,
        subAttr=61,
        score=320,
        noticePrice=300,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 310 low price notice",
        mainAttr=99,
        subAttr=61,
        score=310,
        noticePrice=200,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 low price notice",
        mainAttr=99,
        subAttr=61,
        noticePrice=50,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    # sr 98
    newStrategy(
        name="SR 98 340 low price notice",
        mainAttr=98,
        subAttr=61,
        score=340,
        noticePrice=550,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 330 low price notice",
        mainAttr=98,
        subAttr=61,
        score=330,
        noticePrice=300,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 320 low price notice",
        mainAttr=98,
        subAttr=61,
        score=320,
        noticePrice=200,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 310 low price notice",
        mainAttr=98,
        subAttr=61,
        score=310,
        noticePrice=100,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 low price notice",
        mainAttr=98,
        subAttr=61,
        noticePrice=50,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    # sr
    newStrategy(
        name="SR 99 350 + part time low price notice",
        mainAttr=99,
        noticePrice=70,
        score=350,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 340 + part time low price notice",
        mainAttr=99,
        noticePrice=50,
        score=340,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 330 + part time low price notice",
        mainAttr=99,
        noticePrice=40,
        score=330,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 320 + part time low price notice",
        mainAttr=99,
        noticePrice=30,
        score=320,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 310 + part time low price notice",
        mainAttr=99,
        noticePrice=20,
        score=310,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 99 low price notice",
        mainAttr=99,
        noticePrice=10,
        score=295,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 350+ part time low price notice",
        mainAttr=98,
        noticePrice=60,
        score=350,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 340+ part time low price notice",
        mainAttr=98,
        noticePrice=40,
        score=340,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 330+ part time low price notice",
        mainAttr=98,
        noticePrice=30,
        score=330,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 320+ part time low price notice",
        mainAttr=98,
        noticePrice=20,
        score=320,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98 310+ part time low price notice",
        mainAttr=98,
        noticePrice=10,
        score=310,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 98  part time low price notice",
        mainAttr=98,
        noticePrice=8,
        score=295,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 97 350+ part time low price notice",
        mainAttr=97,
        noticePrice=50,
        score=350,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 97 340+ part time low price notice",
        mainAttr=97,
        noticePrice=30,
        score=340,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 97 330+ part time low price notice",
        mainAttr=97,
        noticePrice=20,
        score=330,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 97 320+ part time low price notice",
        mainAttr=97,
        noticePrice=10,
        score=320,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR 97 part time low price notice",
        mainAttr=97,
        noticePrice=6,
        score=295,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    newStrategy(
        name="SR low part time price notice",
        mainAttr=10,
        noticePrice=5,
        rarity=static_data.RARITY_MAP[static_data.RARITY_SR]),
    # r
    newStrategy(
        name="R 99 part time low price notice",
        mainAttr=99,
        noticePrice=7,
        score=240,
        rarity=static_data.RARITY_MAP[static_data.RARITY_R]),
    newStrategy(
        name="R 98 part time low price notice",
        mainAttr=98,
        noticePrice=6,
        rarity=static_data.RARITY_MAP[static_data.RARITY_R]),
    newStrategy(
        name="R 97 part time low price notice",
        mainAttr=97,
        noticePrice=5,
        rarity=static_data.RARITY_MAP[static_data.RARITY_R]),
    newStrategy(
        name="R part time low price notice",
        mainAttr=10,
        noticePrice=4,
        rarity=static_data.RARITY_MAP[static_data.RARITY_R]),
    # newStrategy(
    #     name="test",
    #     noticePrice=600,
    #     rarity=static_data.RARITY_MAP[static_data.RARITY_R])
]