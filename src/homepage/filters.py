from django.contrib.auth.models import User
import django_filters
from .models import Destinationpackage

class PackageFilter(django_filters.FilterSet):
    class Meta:
        model = Destinationpackage
        fields = {
            'title':['icontains',],
        }
