import datetime as dt
def days(date1,date2):
    date1=dt.datetime.strptime(date1, "%d/%m/%Y")
    date2=dt.datetime.strptime(date2, "%d/%m/%Y")
    dif=int(str(date1-date2).split(" ")[0])
    print(dif)

days("05/02/2021","03/02/2021")
