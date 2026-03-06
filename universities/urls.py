from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet, RankingViewSet

router = DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'rankings', RankingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
