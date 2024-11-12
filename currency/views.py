from rest_framework import filters
from rest_framework import permissions

from core import generics
from currency import models, serializers


class CurrencyView(generics.ReadOnlyModelViewSet):

    serializer_class = serializers.CurrencySerializer
    queryset = models.Currency.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'display_name']
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
