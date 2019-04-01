from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import json
import csv
import django
from celery.decorators import task
from stockprediction.celery import app

def create_ticker_file(ticker):
    temp1=dict(
        model="stockprediction.schema.Stocks",
        pk=1
        )
    temp2=dict(
        stock_id=ticker,
        company = 'MICROSOFT',
        ticker =ticker,
        industry ='Info Tech',
        sector='Software'
    )
    temp1["fields"] = temp2
    d=list()
    d.append(temp1)
    file_name = "./stockprediction/schema/fixtures/"+ticker+".csv"
    with open(file_name,'w+') as tickerfile:
        json.dump(d,tickerfile)

@app.task
def get_data(ticker):
    print("inside")
    ts = TimeSeries(key='XAIXB36ZZ095G9XP', output_format='pandas')
    data, meta_data = ts.get_daily(symbol=ticker, outputsize='full')
    date = data.index.values
    data = data.values.tolist()
    d=list()
    i=1

    for  v in zip(date,data):
        if '2015-01-01' <= v[0] <= '2017-12-31':
            """
            temp1=dict(
            model="stockprediction.HistoricalStockData",
            pk=i
            )
            temp2=dict(
                stock_id=ticker,
                date=v[0],
                open=v[1][0],
                high=v[1][1],
                low=v[1][2],
                close=v[1][3],
                volume=v[1][4]
                )
            temp1["fields"]=temp2
            i+=1
            d.append(temp1)
            """
            d.append((v[0],v[1][0],v[1][1],v[1][2],v[1][3],v[1][4]))
    print("Perfectly Running")
    print(d)
    #if d:
        #print("File written to csv: ",self.writetocsv(d,ticker))

def writetocsv(d,ticker):
    file_name = "./stockprediction/schema/fixtures/"+ticker+"_history.csv"
    with open(file_name,'w+') as history_file:
        file_writer = csv.writer(history_file)
        for row in d:
            file_writer.writerow(row)
        return True
    return False

get_data.delay('MSFT')
