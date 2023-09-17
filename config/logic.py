import json
import requests


# def get_currence_price(ticker):
#     url = 'https://www.cbr-xml-daily.ru/daily_json.js'
#     data = requests.get(url).text
#     data_json = json.loads(data)
#     currency = data_json["Valute"][ticker]["Value"]
#     return currency
#
#
# def get_course(cur1, cur2, value:int):
#     a = get_currence_price(cur1)
#     if cur2 == None or '' or ' ':
#         b = 1
#         c = 'RUB'
#     else:
#         b = get_currence_price(cur2)
#         c = cur2
#     return print(round((a*value / b), 2), c)
#
# get_course('USD', 'EUR', 1)
