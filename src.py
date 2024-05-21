#Importing necessary libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

#Get the necessary inputs ,like stock name or ETF_Exchange Trade Fund. Intervals - Start and End history.
stock=input("Enter the stock name : ").upper()
sdate=input("Enter the starting date(yyyy-mm-dd) : ")
edate=input("Enter the ending date(yyyy-mm-dd) : ")

#Theme customization scripts.
def custom():
  print("Available theme:\n1. Dark.\n2. White.\n3. Ticks.\n4. Darkgrid.\n5. Whitegrid.\n")
  num=int(input("Select theme : "))
  if num==1:
    styleset="dark"
    cl="cyan"
  elif num==2:
    styleset="white"
    cl="red"
  elif num==3:
    styleset="ticks"
    cl="green"
  elif num==4:
    styleset="darkgrid"
    cl="cyan"
  elif num==5:
    styleset="whitegrid"
    cl="blue"
  else:
    print("Invalid theme! Enter available theme.\n")
    custom()
  return styleset,cl



styleset,cl=custom()
symbol = stock
sns.set(style=styleset)

data = yf.download(symbol, start=sdate, end=edate)

data.rename(columns={'Adj Close':'Adj_Close'}, inplace=True)

data['returns'] = data['Adj_Close'].pct_change()

plt.figure(figsize=(10,5))

#Code for multiple_lineplot that shows the peaks and drops of called stocks.
plt.title(f'{symbol} Closing Price', fontsize=16)
sns.lineplot(data=data, x='Date', y='Adj_Close', color=cl , linewidth=1.5)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

#code to show the return of the stocks.
plt.figure(figsize=(10,5))
sns.histplot(data=data, x='returns', binwidth=0.005, color='green')
plt.title('Return Distribution', fontsize=16)
plt.xlabel('Returns', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
