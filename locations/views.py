from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer


# ✅ 1. List All Countries
class CountryListView(ListAPIView):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer


# ✅ 2. List States by Country ISO2
class StateByCountryView(APIView):
    def get(self, request, iso2):
        country = get_object_or_404(Country, iso2=iso2.upper())
        states = country.states.all().order_by('name')
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)


# ✅ 3. List Cities by State ID
class CityByStateView(APIView):
    def get(self, request, state_id):
        state = get_object_or_404(State, id=state_id)
        cities = state.cities.all().order_by('name')
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


# ✅ 4. Search Cities by Query Param (?search=...)
class CitySearchView(ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        search = self.request.GET.get('search', '').strip()
        if search:
            return City.objects.filter(name__icontains=search).order_by('name')
        return City.objects.none()

from django.shortcuts import render

def frontend_view(request):
    return render(request, 'index.html')