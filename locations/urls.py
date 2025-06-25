# urls.py
from django.urls import path
from .views import frontend_view,CountryListView, StateByCountryView, CityByStateView, CitySearchView

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country-list'),
    path('countries/<str:iso2>/states/', StateByCountryView.as_view(), name='states-by-country'),
    path('states/<int:state_id>/cities/', CityByStateView.as_view(), name='cities-by-state'),
    path('cities/', CitySearchView.as_view(), name='city-search'),
    path('',  frontend_view, name='frontend-view'),
]
