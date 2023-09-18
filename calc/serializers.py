import json
import requests

from django.db import models

from rest_framework.serializers import Serializer
from rest_framework.serializers import FloatField

def get_choice_field():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(url).text
    data_json = json.loads(data)
    ticks = data_json['Valute']
    tickers = {}
    for i in ticks:
        tickers[i] = i
    return tickers

class ConverterSerializer(Serializer):
    currency1 = models.CharField(max_length = 3)
    currency2 = models.CharField(max_length = 3)
    value = FloatField()
