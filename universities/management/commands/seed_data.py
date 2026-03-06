import json
import os
from django.core.management.base import BaseCommand
from universities.models import University, Ranking

class Command(BaseCommand):
    help = 'Seed the database with initial university data'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to JSON file to seed from')

    def handle(self, *args, **options):
        file_path = options.get('file') or 'sample_data.json'
        
        if os.path.exists(file_path):
            self.stdout.write(f"Loading data from {file_path}...")
            with open(file_path, 'r') as f:
                data = json.load(f)
        else:
            self.stdout.write(self.style.WARNING(f"File {file_path} not found. Using default hardcoded data."))
            data = [
                {
                    "name": "University of Oxford",
                    "country": "United Kingdom",
                    "city": "Oxford",
                    "website": "https://www.ox.ac.uk",
                    "founded_year": 1096,
                    "rankings": [{"year": 2024, "world_rank": 1, "total_score": 98.5}]
                },
                {
                    "name": "Stanford University",
                    "country": "United States",
                    "city": "Stanford",
                    "website": "https://www.stanford.edu",
                    "founded_year": 1885,
                    "rankings": [{"year": 2024, "world_rank": 2, "total_score": 97.2}]
                }
            ]

        for uni_data in data:
            rankings_data = uni_data.pop('rankings', [])
            university, created = University.objects.get_or_create(
                name=uni_data['name'],
                defaults=uni_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created University: {university.name}'))
            
            for rank_data in rankings_data:
                Ranking.objects.get_or_create(
                    university=university,
                    year=rank_data['year'],
                    defaults={'world_rank': rank_data['world_rank'], 'total_score': rank_data.get('total_score')}
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
