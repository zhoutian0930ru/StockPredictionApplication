from django.shortcuts import render
from django.http import JsonResponse
from .query_db import get_history_data,get_recent_data
from django.core import serializers
import json

# Create your views here.

def get_historical_data(request,ticker):
    data = get_history_data(ticker)
    return JsonResponse(data,safe=False)

def get_current_data(request,ticker):
    data = get_recent_data(ticker)
    return JsonResponse(data,safe=False)
