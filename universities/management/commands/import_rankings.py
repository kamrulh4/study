import csv
import os
from django.core.management.base import BaseCommand
from universities.models import University, Ranking

class Command(BaseCommand):
    help = 'Imports university rankings from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        
        if not os.path.exists(csv_file_path):
            self.stdout.write(self.style.ERROR(f'File "{csv_file_path}" does not exist'))
            return

        with open(csv_file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                # Mapping: institution -> name, country -> country
                university_name = row['institution']
                country = row['country']
                
                university, created = University.objects.get_or_create(
                    name=university_name,
                    defaults={'country': country}
                )
                
                # Mapping: year -> year, world_rank -> world_rank, score -> total_score
                Ranking.objects.update_or_create(
                    university=university,
                    year=int(row['year']),
                    defaults={
                        'world_rank': int(row['world_rank']),
                        'total_score': float(row['score'])
                    }
                )
                count += 1
                
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} ranking records'))
