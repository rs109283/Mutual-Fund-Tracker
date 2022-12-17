import pandas
import numpy
import yfinance as yf
import math
import datetime

import warnings
warnings.filterwarnings("ignore")


total_purchases=[]
mutual_fund_tickers=[]
mutual_fund_investments=[]

class purchase:
    def __init__(self,name,quantity,value,date):
        self.name=name
        self.quantity=float(quantity)
        self.value=float(value)
        self.date=date

def unitCalculator():
    try:
        print("Please type the Ticker")
        ticker=input()
        data=yf.download(ticker)
        print("Please enter the NAV date in YYYY-MM-DD format")
        date=input()
        nav=float('%.4f' % data["Close"][date])
        print("Please enter the amount invested")
        money=float(input())
        money=0.99995*money
        money=float('%.2f' % money)
        units=money/nav
        units=float('%.3f' % units)
        total_purchases.append(purchase(ticker,units,money,date))
    except KeyError:
        print("Inputted the wrong date")
        print("Returning to Main Menu")
        print("-------------------------------------------------------------------")
    

def viewFolio():
    columns=['Row','Ticker','Quantity','Value','Date']
    dummy={'Row','Ticker','Quantity','Value','Date'}
    df=pandas.DataFrame(columns=columns)
    print(df)
    counter=1
    for i in total_purchases:
        df=df.append({'Row':counter,'Ticker':i.name,'Quantity':i.quantity,'Value':i.value,'Date':i.date},ignore_index=True)
        counter+=1
    df=df.to_string(index=False)
    print(df)

def viewGraph():
    temp=total_purchases.sort(key=lambda r: r.date)
    start=temp[0].date
    start=datetime.datetime.strptime(start,'%Y-%m-%d').date()
    end=datetime.date.today()
    difference=(end-start).days
    purchase_counter=0
    for i in range(difference):
        
        if(datetime.datetime.strptime(temp[purchase_counter].date,'%Y-%m-%d')==start+datetime.timedelta(days=i)):
    

condition=True

while condition:
    print("Please input one of the following options")
    print("1. Record the purchase of Mutual Fund")
    print("2. To view all the transactions which have been made")
    print("3. To view the graph of investments")
    choice=int(input())
    if(choice==1):
        unitCalculator()
    elif(choice==2):
        viewFolio()
    elif(choice==3):
        viewGraph()
    else:
        break
         