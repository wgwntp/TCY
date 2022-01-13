import spider
import models
import static_data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # spider.getLeaderInfo()
    lists = spider.getMarketList()
    for l in lists:
        info = l['info']
        baby = models.Baby(info)
        if baby.name == static_data.BABY_NAME_SCAMMER and baby.getTotalAttr() > 360:
            print(l)
        if baby.name == static_data.BABY_NAME_ALTCOIN_COLLECTORE and baby.getTotalAttr() == 341:
            print(l)



