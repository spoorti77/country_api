import json
from django.core.management.base import BaseCommand
from locations.models import Country, State, City
from django.db import transaction

class Command(BaseCommand):
    help = 'Imports countries, states, and cities from JSON files'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("🌍 Starting import...")

        # === Load and import countries ===
        with open('locations/data/countries.json', encoding='utf-8') as f:
            countries = json.load(f)

        for c in countries:
            Country.objects.get_or_create(
                iso2=c['iso2'],
                defaults={
                    'name': c['name'],
                    'iso3': c['iso3'],
                    'iso_numeric': c['numeric_code']
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ Countries imported"))

        # === Load and import states ===
        with open('locations/data/states.json', encoding='utf-8') as f:
            states = json.load(f)

        for s in states:
            try:
                country = Country.objects.get(id=s['country_id'])
            except Country.DoesNotExist:
                continue

            state_code = s.get('state_code') or ''

            State.objects.get_or_create(
                country=country,
                iso2=state_code[:2],
                iso3=state_code[:3],
                iso_numeric=str(s['id'])[:3],
                defaults={
                    'name': s['name']
                }
            )

        self.stdout.write(self.style.SUCCESS("✅ States imported"))

        # === Load and import cities ===
        with open('locations/data/cities.json', encoding='utf-8') as f:
            cities = json.load(f)

        for c in cities:
            try:
                state = State.objects.get(id=c['state_id'])
            except State.DoesNotExist:
                continue

            City.objects.get_or_create(
                name=c['name'],
                state=state
            )

        self.stdout.write(self.style.SUCCESS("✅ Cities imported"))
