
#A class for the routes details

class routes:

    def __init__(self, routeCode, routeName, routeCost, minuteNumIL, minuteNumE):
        self.__routeCode = routeCode
        self.__routeName = routeName
        self.__routeCost = routeCost
        self.__minuteNumIL = minuteNumIL
        self.__minuteNumE = minuteNumE

    @property
    def routeCode(self):
        return self.__routeCode

    @routeCode.setter
    def routeCode(self, value):
        self.__routeCode=value

    @property
    def routeName(self):
        return self.__routeName

    @routeName.setter
    def routeName(self, value):
        self.__routeName = value

    @property
    def routeCost(self):
        return self.__routeCost

    @routeCost.setter
    def routeCost(self, value):
        self.__routeCost = value

    @property
    def minuteNumIL(self):
        return self.__minuteNumIL

    @minuteNumIL.setter
    def minuteNumIL(self, value):
        self.__minuteNumIL = value

    @property
    def minuteNumE(self):
        return self.__minuteNumE

    @minuteNumE.setter
    def minuteNumE(self, value):
        self.__minuteNumE = value

    def print(self):
        print(" route code is: "+self.__routeCode+" route name is: "+self.__routeName+" route is cost: "+
              self.__routeCost+" route con' minutes number in IL is: "+self.__minuteNumIL+" route con' minutes number in E is: "+self.__minuteNumE)
