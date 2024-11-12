import datetime

import pytz
from rest_framework import serializers

from currency import models


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Currency
        fields = (
            'display_name',
            'code',
            'symbol',
        )
