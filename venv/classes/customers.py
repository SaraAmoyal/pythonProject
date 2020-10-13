'''CREATE TABLE [dbo].[customers_tbl](
	[custCode] [int] primary key IDENTITY(100,1) NOT NULL,
	[custId][varchar](9),
	[custFirstName] [varchar](50) ,
	[custLastName] [varchar](50) ,
	[custAddress] [varchar](50),
	[custCountry] [varchar](20)
)'''
#A class for the customers details
class customers:

    def __init__(self, custCode, custId, custFirstName, custLastName, custAddress, custCountry, kavimList):
        self.__custCode = custCode
        self.__custId = custId
        self.__custFirstName = custFirstName
        self.__custLastName = custLastName
        self.__custAddress=custAddress
        self.__custCountry=custCountry
        self.__kavimList=kavimList

    @property
    def custCode(self):
        return self.__custCode

    @custCode.setter
    def custCode(self, value):
        self.__custCode=value

    @property
    def custId(self):
        return self.__custId

    @custCode.setter
    def custCode(self, value):
        self.__custCode=value

    @property
    def custFirstName(self):
        return self.__custFirstName

    @custFirstName.setter
    def custFirstName(self, value):
        self.__custFirstName=value

    @property
    def custLastName(self):
        return self.__custLastName

    @custLastName.setter
    def custLastName(self, value):
        self.__custLastName=value

    @property
    def custAddress(self):
        return  self.__custAddress

    @custAddress.setter
    def custAddress(self, value):
        self.__custAddress=value

    @property
    def custCountry(self):
        return self.__custCountry

    @custCountry.setter
    def custCountry(self, value):
        self.__custCountry=value

    @property
    def kavimList(self):
        return self.__kavimList

    @kavimList.setter
    def kavimList(self, value):
        self.__kavimList=value

    def print(self):
        print("customer code is: "+self.__custCode+", customer id is: "+self.__custId+", customer name is: "+
              self.__custFirstName+" "+self.__custLastName+", customer address is: "+self.__custAddress+", customer country is: "+self.__custCountry+".")
