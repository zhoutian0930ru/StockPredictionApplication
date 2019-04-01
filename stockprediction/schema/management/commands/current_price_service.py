from __future__ import unicode_literals
from collections import defaultdict
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from ...models import RecentStockData,Stocks
import schedule
import time
import requests
from django.core.management.base import BaseCommand
from django.utils.encoding import force_text


class CurrentData:

    def __init__(self):
        self.key="XAIXB36ZZ095G9XP"
        self.function="TIME_SERIES_INTRADAY"
        self.interval="1min"
        self.last_refreshed=defaultdict(int)
        self.stored_values=defaultdict(list)

    def get_current_data(self,ticker):


        URL="https://www.alphavantage.co/query"
        PARAMS=dict(
            function=self.function,
            symbol=ticker,
            interval=self.interval,
            apikey=self.key
        )
        r = requests.get(url=URL, params=PARAMS)
        r=r.json()
        #print("last refreshed: ",self.last_refreshed[ticker])
        #print("meta refresh: ",r['Meta Data']['3. Last Refreshed'])
        if not (bool(self.last_refreshed[ticker])) or (bool(self.last_refreshed[ticker]) and\
        r['Meta Data']['3. Last Refreshed']>self.last_refreshed[ticker]):
            d=[]
            #print("Inside if condition")
            for key,value in r['Time Series (1min)'].items():
                if not bool((self.last_refreshed[ticker])) or key>self.last_refreshed[ticker] :
                    t=(key,float(value['1. open']),float(value['2. high']),
                    float(value['3. low']),float(value['4. close']),
                    float(value['5. volume']))
                    d.append(t)
            self.stored_values[ticker] = d+self.stored_values[ticker]
            #print("ticker: ",ticker)
            #print("length: ",len(self.stored_values[ticker]))
            self.last_refreshed[ticker]=r['Meta Data']['3. Last Refreshed']
            if len(self.stored_values[ticker]) >= 100:
                #print("Uploading data to database")
                self.upload_to_database(self.stored_values[ticker],ticker)

    def upload_to_database(self,values_to_upload,ticker):
        s1 = Stocks(stock_id=ticker, company="MICROSOFT", ticker =ticker,
        industry="IT", sector="Software")
        print("Uploading data")
        for t in values_to_upload:
            data, created = RecentStockData.objects.get_or_create(
                stock_id=s1,
                date=force_text(t[0]),
                open=force_text(t[1]),
                high=force_text(t[2]),
                low=force_text(t[3]),
                close=force_text(t[4]),
                volume=force_text(t[5])
            )

        self.stored_values[ticker]=[]


class Command(BaseCommand):

    def handle(self, *args, **options):
        obj = CurrentData()
        #count=0
        while True:
            tickers=['MSFT','GOOG']
            for ticker in tickers:
                obj.get_current_data(ticker)
            #count+=1
            #print("count: ",count)
            time.sleep(60)
