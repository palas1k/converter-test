from drf_spectacular.utils import extend_schema, OpenApiParameter

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from calc.serializers import ConverterSerializer
from calc.utils import get_course, get_choice_field


class CurrencyConverter(APIView):
    serializer_class = ConverterSerializer

    @extend_schema(
        parameters=[OpenApiParameter('from_currency', enum=get_choice_field()), OpenApiParameter('to_currency', enum=get_choice_field()),
                    OpenApiParameter('value', float)])
    def get(self, request):
        serializer = ConverterSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        cur1 = serializer.data['from_currency']
        cur2 = serializer.data['to_currency']
        value = serializer.data['value']
        data = round(get_course(cur1, cur2, value), 2)
        return Response(data=data, status=status.HTTP_200_OK)
