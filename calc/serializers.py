from rest_framework.serializers import Serializer
from rest_framework.serializers import FloatField, CharField

class ConverterSerializer(Serializer):
    from_currency = CharField()
    to_currency = CharField(allow_null=True, required=False)
    value = FloatField(min_value=0.1)
