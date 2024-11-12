import operator
from functools import reduce

import pytz
from django.db.models import Q, Count
# from rest_framework import filters
# from rest_framework import permissions

# from core import generics
from country import models
from country import serializers


# class FilterTimezone(filters.SearchFilter):
#     search_param = 'timezone'

#     def filter_queryset(self, request, queryset, view):
#         search_terms = self.get_search_terms(request)

#         if not search_terms:
#             return queryset

#         queries = []
#         for code, timezones in pytz.country_timezones.items():
#             for timezone in timezones:
#                 for search_term in search_terms:
#                     if search_term in timezone:
#                         queries.append(Q(code__istartswith=code))
#         if queries:
#             queryset = queryset.filter(reduce(operator.or_, queries))
#         return queryset


# class FilterCountry(filters.SearchFilter):
#     search_param = 'id'

#     def filter_queryset(self, request, queryset, view):
#         search_terms = self.get_search_terms(request)

#         if not search_terms:
#             return queryset
#         if all(x.isnumeric() for x in search_terms):
#             queryset = queryset.filter(id__in=search_terms)
#         return queryset


# class CountryView(generics.ReadOnlyModelViewSet):

#     serializer_class = serializers.CountrySerializer
#     queryset = models.Country.objects.all()
#     permission_classes = (permissions.AllowAny,)
#     authentication_classes = ()
#     filter_backends = [filters.SearchFilter, FilterTimezone, FilterCountry]
#     search_fields = ['name', 'code']
