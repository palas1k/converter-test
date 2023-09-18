import json
import requests

def get_choice_field():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(url).text
    data_json = json.loads(data)
    ticks = data_json['Valute']
    tickers = {}
    for i in ticks:
        tickers[i] = i
    return tickers


def get_currence_price(ticker):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(url).text
    data_json = json.loads(data)
    currency = data_json["Valute"][ticker]["Value"]
    return float(currency)


def get_course(cur1, cur2, value):
    a = get_currence_price(cur1)
    if cur2 != None:
        b = get_currence_price(cur2)
        return (a / b) * float(value)
    return a
