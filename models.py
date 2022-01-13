import static_data


class Attr:
    def __init__(self):
        self.index = -1
        self.name = ""
        self.value = ""
        # 0：main 1:sub 2:normal
        self.attrType = -1


class Baby:
    def __init__(self, info):
        self.nftIndex = info['nftIndex']
        self.name = static_data.NAME_MAP[self.nftIndex]
        self.attrs = info['attributes']
        self.rarity = static_data.RARITY_MAP[info['rarity']]
        self.level = info['level']
        self.mAttr = [Attr() for i in range(6)]
        n = 0
        for a in self.attrs:
            self.mAttr[n].index = n
            self.mAttr[n].name = static_data.ATTRS_MAP[n]
            self.mAttr[n].value = a
            # 2 : normal
            aType = static_data.ATTR_TYPE_NORMAL
            if static_data.MAIN_ATTR_MAP[self.nftIndex] == n:
                # 0 ： mainType
                aType = static_data.ATTR_TYPE_MAIN
            elif static_data.SUB_ATTR_MAP[self.nftIndex] == n:
                # 1 : mainType
                aType = static_data.ATTR_TYPE_SUB
            self.mAttr[n].attrType = aType

    def getMainAttr(self):
        return self.attrs[static_data.MAIN_ATTR_MAP[self.nftIndex]]

    def getSubAttr(self):
        return self.attrs[static_data.SUB_ATTR_MAP[self.nftIndex]]

    def getTotalAttr(self):
        score = 0
        for attr in self.attrs:
            score += attr
        return score

    def printBaby(self):
        print()


class Strategy:
    def __init__(self):
        self.name = ""
        self.babyName = ""
        self.token = ""
        self.noticePrice = 99999
        self.mainAttr = 0
        self.subAttr = 0
        self.level = 1
        self.score = 0
        self.rarity = -1
