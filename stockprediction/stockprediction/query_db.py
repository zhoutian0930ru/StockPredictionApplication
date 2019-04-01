from schema.models import HistoricalStockData,RecentStockData,Stocks
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from collections import OrderedDict

def get_history_data(ticker):
    data = HistoricalStockData.objects.all()
    response=dict()
    for val in data.filter(stock_id=ticker):
        d=dict(
            open=val.open,
            high=val.high,
            low=val.low,
            close=val.close,
            volume=val.volume
        )
        response[val.date.strftime("%d/%m/%Y %H:%M:%S")[:-9]]=d
    response=OrderedDict(sorted(response.items(), \
    key= lambda t:datetime.datetime.strptime(t[0],"%d/%m/%Y"),reverse=True))
    serialized_q = json.dumps(response, cls=DjangoJSONEncoder)
    return response

def get_recent_data(ticker):
    data = RecentStockData.objects.all()
    response=dict()
    for val in data.filter(stock_id=ticker):
        d=dict(
            open=val.open,
            high=val.high,
            low=val.low,
            close=val.close,
            volume=val.volume
        )
        response[val.date.strftime("%d/%m/%Y %H:%M:%S")]=d
    response=OrderedDict(sorted(response.items(), \
    key= lambda t:datetime.datetime.strptime(t[0],"%d/%m/%Y %H:%M:%S"),reverse=True))
    serialized_q = json.dumps(response, cls=DjangoJSONEncoder)
    return response
