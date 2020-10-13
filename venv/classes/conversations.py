import datetime
#A class for the conversations details

class conversations:
    cntConversations=0
    def __init__(self, convCode, startDate, endDate, fromTel, toTel):
        conversations.cntConversations+=1
        self.__convCode = convCode
        self.__startDate=startDate
        self.__endDate=endDate
        self.__fromTel=fromTel
        self.__toTel=toTel

    @property
    def convCode(self):
        return self.__convCode

    @convCode.setter
    def convCode(self, value):
        self.__convCode=value

    @property
    def startDate(self):
        return  self.__startDate

    @startDate.setter
    def startDate(self, value):
        self.__startDate=value

    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, value):
        self.__endDate=value

    @property
    def fromTel(self):
        return self.__fromTel

    @fromTel.setter
    def fromTel(self, value):
        self.__fromTel=value

    @property
    def toTel(self):
        return self.__toTel

    @toTel.setter
    def toTel(self, value):
        self.__toTel=value

    def print(self):
        print(" conv' code is: "+self.__convCode+" conv' start date is: "+self.__startDate+" conv' end date is: "+
              self.__endDate+" conv' called from tel number: "+self.__fromTel+" conv' call to tel number: "+self.__toTel)


    def __eq__(self, other):
        if self.__endDate-self.__startDate==other.__endDate-other.__startDate:
            return true
        return false

    def __uneq__(self, other):
        if self.__endDate-self.__startDate!=other.__endDate-other.__startDate:
            return true
        return false




