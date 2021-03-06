import django_filters
from backend.apps.film.models import Film, Genre ,Celebrity
from django import forms

class FilmFilter(django_filters.FilterSet):
    genres = django_filters.ModelChoiceFilter(
        field_name="genres",
        queryset=Genre.objects.all(),
        widget=forms.Select()
    )
    date_relise = django_filters.NumberFilter(
        field_name='date_relise', lookup_expr='year'
    )

    class Meta:
        model = Film
        fields = [
            'genres',
            'date_relise',
            ]


class CelebrityFilter(django_filters.FilterSet):
    birthday = django_filters.NumberFilter(
        field_name='birthday', lookup_expr='year'
    )

    class Meta:
        model = Celebrity
        fields = [
            'birthday',
            ]
