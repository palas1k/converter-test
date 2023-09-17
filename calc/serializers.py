import json
import requests
from django.db import models
from django.forms import ChoiceField

from rest_framework.serializers import Serializer
from rest_framework.serializers import FloatField

def get_choice_field():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(url).text
    data_json = json.loads(data)
    ticks = data_json['Valute']
    tickers = tuple()
    for i in ticks:
        tickers = tickers + (i,i)
    return tickers

CHOICE = get_choice_field()



class ConverterSerializer(Serializer):
    currency1 = ChoiceField(choices = CHOICE)
    currency2 = ChoiceField(choices = CHOICE)
    value = FloatField(min_value=1)
