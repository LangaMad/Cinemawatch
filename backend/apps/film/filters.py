import django_filters
from backend.apps.film.models import Film
from django import forms

class FilmFilter(django_filters.FilterSet):


    genre = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )


    class Meta:
        model = Film
        fields = [
            'name'
            ]
