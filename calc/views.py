import json
import requests
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.fields import ChoiceField
from rest_framework.response import Response
from rest_framework.views import APIView

from calc.serializers import ConverterSerializer, get_choice_field


def get_currence_price(ticker):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    data = requests.get(url).text
    data_json = json.loads(data)
    currency = data_json["Valute"][ticker]["Value"]
    return float(currency)


def get_course(cur1, cur2, value):
    a = get_currence_price(cur1)
    b = get_currence_price(cur2)
    c = cur2
    return (a/b)*float(value)


class CurrencyConverter(APIView):
    serializer_class = ConverterSerializer

    @extend_schema(
        parameters=[OpenApiParameter('from', enum=get_choice_field()), OpenApiParameter('to', enum=get_choice_field()), OpenApiParameter('value', float)])
    def get(self, request):
        cur1 = request.GET.get('from').upper()
        cur2 = request.GET.get('to').upper()
        value = request.GET.get('value')
        if value == None:
            value = 1
        data = round(get_course(cur1, cur2, value), 2)
        return Response(data=data, status=status.HTTP_200_OK)
