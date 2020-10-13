                        

CREATE TABLE [dbo].[customers_tbl](
	[custCode] [int] primary key IDENTITY(100,1) NOT NULL,
	[custId][varchar](9),
	[custFirstName] [varchar](50) ,
	[custLastName] [varchar](50) ,
	[custAddress] [varchar](50),
	[custCountry] [varchar](20)
)

CREATE TABLE [dbo].[kavim_tbl](
	[kavCode] [int] identity(200, 1) primary key NOT NULL,
	[custCode] [int] foreign key references customers_tbl(custCode) NOT NULL,
	[kavRoute] [int] not null,
	[kavNumber][varchar](10) not null
)

CREATE TABLE [dbo].[routes_tbl](
	[routeCode] [int] primary key identity(300, 2) NOT NULL,
	[routeName] [varchar](30) ,
	[routeCost] [int]  NOT NULL,
	[minuteNumIL] [int] NOT NULL,
	[minuteNumE][int] not null
)


create table [dbo].[conversations_tbl](
     [convCode][int] primary key identity(400, 1) not null,
	 [startDate][datetime],
	 [endDate][datetime],
	 [fromTel][varchar](10),
	 [toTel][varchar](10)
)

INSERT [dbo].[customers_tbl] ([custId], [custFirstName], [custLastName], [custAddress], [custCountry]) VALUES ('206831166', 'sara', 'amoyal', 'Hazon Hish', 'israel')
INSERT [dbo].[customers_tbl] ([custId], [custFirstName], [custLastName], [custAddress], [custCountry]) VALUES ('031390487', 'hana', 'amoyal', 'Hazon Hish', 'israel')
INSERT [dbo].[customers_tbl] ([custId], [custFirstName], [custLastName], [custAddress], [custCountry]) VALUES ('106831166', 'lea', 'amoyal', 'harav shach', 'france')
INSERT [dbo].[customers_tbl] ([custId], [custFirstName], [custLastName], [custAddress], [custCountry]) VALUES ('131390487', 'ester', 'amoyal', 'avney nezer', 'belgy')

insert [dbo].[routes_tbl] ([routeName], [routeCost], [minuteNumIL], [minuteNumE]) values ('one', 25, 7000, 100)
insert [dbo].[routes_tbl] ([routeName], [routeCost], [minuteNumIL], [minuteNumE]) values ('twe', 17, 3000, 200)
insert [dbo].[routes_tbl] ([routeName], [routeCost], [minuteNumIL], [minuteNumE]) values ('three', 20, 5000, 100)
insert [dbo].[routes_tbl] ([routeName], [routeCost], [minuteNumIL], [minuteNumE]) values ('four', 15, 2000, 100)

insert [dbo].[kavim_tbl] ([custCode], [kavRoute], [kavNumber]) values (101, 302, '0533163641')
insert [dbo].[kavim_tbl] ([custCode], [kavRoute], [kavNumber]) values (102, 304, '0583262914') 
insert [dbo].[kavim_tbl] ([custCode], [kavRoute], [kavNumber]) values (103, 306, '0533162914') 
insert [dbo].[kavim_tbl] ([custCode], [kavRoute], [kavNumber]) values (103, 306, '0533162955') 
insert [dbo].[kavim_tbl] ([custCode], [kavRoute], [kavNumber]) values (102, 308, '0533162514') 
 
insert [dbo].[conversations_tbl] ([startDate], [endDate], [fromTel], [toTel]) values ('2011.03.12 19:17:22.242', '2011.03.12 19:55:25.233', '0533162914', '0583262914')
insert [dbo].[conversations_tbl] ([startDate], [endDate], [fromTel], [toTel]) values ('2011.03.12 03:22:21.443', '2011.03.12 03:23:12.333', '0533162914', '0583262914')
insert [dbo].[conversations_tbl] ([startDate], [endDate], [fromTel], [toTel]) values ('2011.03.12', '2011.03.12', '0533163641', '0583262914')
insert [dbo].[conversations_tbl] ([startDate], [endDate], [fromTel], [toTel]) values ('2011.03.12', '2011.03.12', '0533163641', '0583262914')




