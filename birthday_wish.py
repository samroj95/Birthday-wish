from datetime import datetime as dt
def valDate(input):
    try:
        dateobject=dt.strptime(input,'%d/%m/%y')
        return True
    except ValueError:
        return False
date=input("Enter you birthday date->dd/mm/yy:")
a=valDate(date)
if a==True:
    print("Happy birthday...")
else:
    print("Best wishes for your birthday in advance..")