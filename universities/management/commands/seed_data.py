import json
import os
import csv
from django.core.management.base import BaseCommand
from universities.models import University, Ranking

class Command(BaseCommand):
    help = 'Seed the database with initial university data'

    def add_arguments(self, parser):
        parser.add_argument('--file', type=str, help='Path to data file (JSON or CSV) to seed from')

    def handle(self, *args, **options):
        file_path = options.get('file') or 'sample_data.csv'
        
        if not os.path.exists(file_path):
            # Fallback to JSON if CSV not found and no specific file provided
            if not options.get('file') and os.path.exists('sample_data.json'):
                file_path = 'sample_data.json'
            else:
                self.stdout.write(self.style.ERROR(f"File {file_path} not found."))
                return

        self.stdout.write(f"Loading data from {file_path}...")

        if file_path.endswith('.json'):
            self.seed_from_json(file_path)
        elif file_path.endswith('.csv'):
            self.seed_from_csv(file_path)
        else:
            self.stdout.write(self.style.ERROR(f"Unsupported file format: {file_path}"))

    def seed_from_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
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
        self.stdout.write(self.style.SUCCESS('Successfully populated from JSON'))

    def seed_from_csv(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                # Mapping QS 2026 CSV columns
                name = row.get('Institution Name')
                country = row.get('Country/Territory')
                rank_str = row.get('2026 Rank')
                score_str = row.get('Overall SCORE')
                
                if not name or not country:
                    continue

                # Clean rank (handle "701-710" or "801+" by taking the first number)
                try:
                    rank = int(''.join(filter(str.isdigit, rank_str.split('-')[0].split('+')[0])))
                except (ValueError, TypeError):
                    continue

                # Clean score
                try:
                    score = float(score_str) if score_str and score_str != '-' else None
                except ValueError:
                    score = None

                university, created = University.objects.get_or_create(
                    name=name,
                    defaults={'country': country}
                )
                
                Ranking.objects.update_or_create(
                    university=university,
                    year=2026,
                    defaults={'world_rank': rank, 'total_score': score}
                )
                count += 1
            
            self.stdout.write(self.style.SUCCESS(f'Successfully populated {count} entries from CSV'))
