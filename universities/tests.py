from django.test import TestCase, Client
from django.urls import reverse
from .models import University, Ranking
import json

class UniversityAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.university = University.objects.create(
            name="Test Uni",
            country="Test Country",
            city="Test City"
        )
        self.ranking = Ranking.objects.create(
            university=self.university,
            year=2024,
            world_rank=10,
            total_score=85.0
        )

    def test_get_universities(self):
        # In Ninja, the URL might not have a name by default if not specified
        # But we can call the endpoint directly or add names to routes
        response = self.client.get('/api/v1/universities')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(len(data) >= 1)
        self.assertEqual(data[0]['name'], "Test Uni")

    def test_get_rankings(self):
        response = self.client.get('/api/v1/rankings')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(len(data) >= 1)
