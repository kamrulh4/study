from django.core.management.base import BaseCommand
from universities.models import University, Ranking

class Command(BaseCommand):
    help = 'Seed the database with initial university data'

    def handle(self, *args, **options):
        data = [
            {
                "name": "University of Oxford",
                "country": "United Kingdom",
                "city": "Oxford",
                "website": "https://www.ox.ac.uk",
                "founded_year": 1096,
                "rankings": [{"year": 2024, "world_rank": 1, "total_score": 98.5}, {"year": 2023, "world_rank": 1, "total_score": 98.4}]
            },
            {
                "name": "Stanford University",
                "country": "United States",
                "city": "Stanford",
                "website": "https://www.stanford.edu",
                "founded_year": 1885,
                "rankings": [{"year": 2024, "world_rank": 2, "total_score": 97.2}, {"year": 2023, "world_rank": 3, "total_score": 96.8}]
            },
            {
                "name": "Massachusetts Institute of Technology",
                "country": "United States",
                "city": "Cambridge",
                "website": "https://www.mit.edu",
                "founded_year": 1861,
                "rankings": [{"year": 2024, "world_rank": 3, "total_score": 96.9}, {"year": 2023, "world_rank": 2, "total_score": 97.4}]
            },
            {
                "name": "University of Cambridge",
                "country": "United Kingdom",
                "city": "Cambridge",
                "website": "https://www.cam.ac.uk",
                "founded_year": 1209,
                "rankings": [{"year": 2024, "world_rank": 4, "total_score": 95.8}]
            },
            {
                "name": "Harvard University",
                "country": "United States",
                "city": "Cambridge",
                "website": "https://www.harvard.edu",
                "founded_year": 1636,
                "rankings": [{"year": 2024, "world_rank": 5, "total_score": 95.1}]
            }
        ]

        for uni_data in data:
            rankings_data = uni_data.pop('rankings')
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
                    defaults={'world_rank': rank_data['world_rank'], 'total_score': rank_data['total_score']}
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
