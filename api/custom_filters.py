# we need to inherit filterset in django filter and overide the methods
from django_filters import FilterSet
from django.contrib.auth.models import User
from django_filters.rest_framework import NumberFilter, CharFilter


class UserFilter(FilterSet):
    # map the names with the fields
    pk = NumberFilter('id') # /?id=1
    is_active = CharFilter('is_active') # /?is_active=Trues
    profile = NumberFilter('profile__id') # /?profile=1
    min_age = NumberFilter(method='filter_by_min_age')
    max_age = NumberFilter(method='filter_by_max_age')
    
    class Meta:
        model = User
        # we ddeclare the filter names here like ?username=tesr so username can be created as filter
        # the fields can be named anything but they need to be mapped with the correct field in the model
        fields = ('pk', 'is_active', 'profile')
    
    def filter_by_min_age(self, queryset, filter_name, value):
        return queryset.filter(profile__age__gte=value)
    
    def filter_by_max_age(self, queryset, filter_name, value):
        return queryset.filter(profile__age__lte=value)