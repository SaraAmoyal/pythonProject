
#A class for the kavim details
class kavim:

    def __init__(self, kavCode, custCode, kavRoute, kavNumber):
        self.__kavCode = kavCode
        self.__custCode = custCode
        self.__kavRoute = kavRoute
        self.__kavNumber = kavNumber

    @property
    def kavCode(self):
        return self.__kavCode

    @kavCode.setter
    def kavCode(self, value):
        self.__kavCode=value

    @property
    def custCode(self):
        return self.__custCode

    @custCode.setter
    def custCode(self, value):
        self.__custCode = value

    @property
    def kavRoute(self):
        return self.__kavRoute

    @kavRoute.setter
    def kavRoute(self, value):
        self.__kavRoute = value

    @property
    def kavNumber(self):
        return self.__kavNumber

    @kavNumber.setter
    def kavNumber(self, value):
        self.__kavNumber = value

    def print(self):
        print("kav code is: "+self.__kavCode+" cust code is: "+self.__custCode+" kav route is: "+self.__kavRoute+" kav number is: "+self.__kavNumber)
