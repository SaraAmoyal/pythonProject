# Manage the system by choosing screen and navigation

from classes.conversations import conversations
import SqlConnection
import datetime


def create_conv():
    # create a conversation that ended now, get the start time and the call numbers from the user
    hour=int(input("enter the start hour: "))
    min=int(input("enter the start minute: "))
    endDate = datetime.datetime.now()
    startDate=datetime.datetime(endDate.year, endDate.month, endDate.day, hour, min)
    fromTel=input("enter tel number to call from. ")
    toTel=input("enter tel number to call to. ")
    conv=conversations(111, startDate, endDate, fromTel, toTel)
    answer=SqlConnection.create_conv(conv)
    print(answer)

def disp_your_conversations():
    telNumber=input('enter your fhone number: ')
    allConv=SqlConnection.convs_by_telnumber(telNumber)
    for conv in allConv:
        print(str(conv.startDate)+', '+str(conv.endDate)+', '+conv.fromTel+', '+conv.toTel)

def disp_amount_to_pay():
    id=input('enter yuor id number')
    kavimList=SqlConnection.get_cust_kavimList(id)
    costList=SqlConnection.get_cost_for_kavimList(kavimList)
    print("the amount to pay is: "+str(sum(costList))+"NIS")

def cnt_kavim_for_every_route():
    cntList=SqlConnection.cnt_kavim_for_every_route()
    print(cntList)


def check_exceeding_for_kav():
    kavNumber=input("enter kav number")
    print(SqlConnection.check_exceeding_for_kav(kavNumber))


def call_func_by_choosing(c):
    if c==1:
        create_conv(),
    elif c==2:
        disp_your_conversations(),
    elif c==3:
        disp_amount_to_pay(),
    elif c==4:
        cnt_kavim_for_every_route(),
    elif c==5:
        check_exceeding_for_kav(),
    elif c==6:
        exit()


def mainPage():
# this function create a choosing screen and navigates in the system

    choosing=0
    while choosing!=6:

        choosing=input('Please choose:\n'
          '1-to create new conversation\n'
          '2-to display your conversations\n'
          '3-to display your amount to pay\n'
          '4-to check how many kavim there are for every route\n'
          '5-check if a kav exceeded from its minutes number\n'
          '6-exit')
        call_func_by_choosing(int(choosing))


mainPage()
