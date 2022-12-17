import pandas
import numpy
import yfinance as yf
import math

total_purchases=[]

class purchase:
    def __init__(self,name,quantity,value,date):
        self.name=name
        self.quantity=quantity
        self.value=value
        self.date=date

condition=True

while condition:
    print("Please input one of the following options")
    print("1. Record the purchase of Mutual Fund")
    choice=input()
    choice=1
    if(choice==1):
        try:
            print("Please type the Ticker")
            ticker=input()
            data=yf.download(ticker)
            # print(data)
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
            condition=0
        except KeyError:
            print("Inputted the wrong date")
            print("Returning to Main Menu")
            print("-------------------------------------------------------------------")
