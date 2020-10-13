# Connection to sql database

import pyodbc
import datetime
import classes.customers
import classes.kavim
import classes.Routes
import classes.conversations
import sqlite3

Server='KF\MSSQLSERVER02'
database='pythonKavim'
uname='KF/USER'
connection =pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; Server='+Server+';DATABASE='+database+';UID='+uname+';PWD=null;;Trusted_Connection=yes')

def create_conv(conv):
    try:
        cursor = connection.cursor()
        sql_insert = """insert into conversations_tbl (startDate, endDate, fromTel, toTel) values (?, ?, ?, ?);"""
        data_tuple = (conv.startDate, conv.endDate, conv.fromTel, conv.toTel)
        cursor.execute(sql_insert, data_tuple)
        cursor.close()
    except:
        return "error in execution!"
    finally:
        cursor.close()
    connection.commit()
    return "success!!"


def convs_by_telnumber(number):
    try:
        cursor = connection.cursor()
        cursor.execute("select * from [dbo].[conversations_tbl] where [fromTel]=" + number)
        allConv = cursor.fetchall()
        cursor.close()
    except:
        return "error in execution!"
    finally:
        cursor.close()
    return allConv

def get_cust_kavimList(id):
    try:
        cursor = connection.cursor()
        cursor.execute(""
                          "select k.* from [dbo].[customers_tbl] c join [dbo].[kavim_tbl] k"
                          " on c.custCode=k.custCode where c.custId=" + id)
        allKavim = cursor.fetchall()
        cursor.close()
    except:
        return "error in execution!"
    finally:
        cursor.close()
    return allKavim

def get_cost_for_kavimList(kavimList):
    try:
        cursor = connection.cursor()
        allKavim = []
        for k in kavimList:
            route = str(k.kavRoute)
            cursor.execute("select routeCost from [dbo].[routes_tbl] where [routeCode]=" + route)
            for [routeCost] in cursor:
                allKavim.append(routeCost)
        cursor.close()
    except:
        return "error in execution!"
    finally:
        cursor.close()

    return allKavim

def cnt_kavim_for_every_route():
    try:
        cursor = connection.cursor()
        cursor.execute(
            "select [routeName], count(*) from [dbo].[kavim_tbl] k join [dbo].[routes_tbl] r on k.kavRoute=r.routeCode group by routeName")
        cnt_list = cursor.fetchall()
        cursor.close()
    except:
        return "error in execution!"
    finally:
        cursor.close()
    return cnt_list

def check_exceeding_for_kav(kavNumber):
    minutesNum=0
    try:
        cursor=connection.cursor()
        use_minutes_number=cursor.execute("select sum(datediff(n, startDate, endDate)) as usedMin from [dbo].[conversations_tbl] where fromTel="+kavNumber)
        for [usedMin] in use_minutes_number:
            usedMinutes=usedMin
        minuteNumCursor=cursor.execute("""select minuteNumIL  
        from routes_tbl r join [dbo].[kavim_tbl] k on r.[routeCode]= k.kavRoute 
        where kavNumber="""+kavNumber)
        for [minuteNumIL] in minuteNumCursor:
            minutesNum=minuteNumIL
        cursor.close()
    except:
        return "error in execution!"
    finally:
        cursor.close()
    if minutesNum>=usedMinutes:
        return "didn't exceeded"
    else:
        return "yes it exceeded"







