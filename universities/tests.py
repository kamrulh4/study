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
        response = self.client.get('/api/v1/universities')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(len(data) >= 1)
        self.assertEqual(data[0]['name'], "Test Uni")

    def test_create_university_unauthorized(self):
        payload = {
            "name": "Unauthorized Uni",
            "country": "Country",
            "city": "City"
        }
        response = self.client.post('/api/v1/universities', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_create_university_authorized(self):
        payload = {
            "name": "Authorized Uni",
            "country": "Country",
            "city": "City"
        }
        headers = {'HTTP_AUTHORIZATION': 'Bearer ninja-token-2024'}
        response = self.client.post('/api/v1/universities', data=json.dumps(payload), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.content)
        self.assertEqual(data['name'], "Authorized Uni")

    def test_update_university(self):
        payload = {"city": "New City"}
        headers = {'HTTP_AUTHORIZATION': 'Bearer ninja-token-2024'}
        response = self.client.put(f'/api/v1/universities/{self.university.id}', data=json.dumps(payload), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['city'], "New City")

    def test_delete_university(self):
        headers = {'HTTP_AUTHORIZATION': 'Bearer ninja-token-2024'}
        response = self.client.delete(f'/api/v1/universities/{self.university.id}', **headers)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(University.objects.filter(id=self.university.id).exists())

class RankingAPITests(TestCase):
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

    def test_get_rankings(self):
        response = self.client.get('/api/v1/rankings')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)

    def test_create_ranking(self):
        payload = {
            "university": self.university.id,
            "year": 2025,
            "world_rank": 5,
            "total_score": 90.0
        }
        headers = {'HTTP_AUTHORIZATION': 'Bearer ninja-token-2024'}
        response = self.client.post('/api/v1/rankings', data=json.dumps(payload), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.content)
        self.assertEqual(data['year'], 2025)

    def test_update_ranking(self):
        payload = {"total_score": 95.0}
        headers = {'HTTP_AUTHORIZATION': 'Bearer ninja-token-2024'}
        response = self.client.put(f'/api/v1/rankings/{self.ranking.id}', data=json.dumps(payload), content_type='application/json', **headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['total_score'], 95.0)

    def test_delete_ranking(self):
        headers = {'HTTP_AUTHORIZATION': 'Bearer ninja-token-2024'}
        response = self.client.delete(f'/api/v1/rankings/{self.ranking.id}', **headers)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Ranking.objects.filter(id=self.ranking.id).exists())
