from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import University, Ranking
from .serializers import UniversitySerializer, RankingSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all().prefetch_related('rankings')
    serializer_serializer = UniversitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'city']

    def get_serializer_class(self):
        return UniversitySerializer

class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'world_rank']
