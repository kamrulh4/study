from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import University, Ranking

class UniversityAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
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
        url = reverse('university-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response.data is a list when pagination is off
        self.assertTrue(len(response.data) >= 1)

    def test_get_rankings(self):
        url = reverse('ranking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
