from typing import List
from ninja import NinjaAPI, Schema, ModelSchema
from django.shortcuts import get_object_or_404
from .models import University, Ranking

api = NinjaAPI(title="University Ranking API (Django Ninja)")

class RankingSchema(ModelSchema):
    class Meta:
        model = Ranking
        fields = ['id', 'year', 'world_rank', 'total_score']

class UniversitySchema(ModelSchema):
    rankings: List[RankingSchema] = []
    
    class Meta:
        model = University
        fields = ['id', 'name', 'country', 'city', 'website', 'founded_year', 'rankings']

class UniversityCreateSchema(Schema):
    name: str
    country: str
    city: str
    website: str = None
    founded_year: int = None

@api.get("/universities", response=List[UniversitySchema])
def list_universities(request):
    return University.objects.all().prefetch_related('rankings')

@api.get("/universities/{university_id}", response=UniversitySchema)
def get_university(request, university_id: int):
    return get_object_or_404(University, id=university_id)

@api.post("/universities", response=UniversitySchema)
def create_university(request, data: UniversityCreateSchema):
    university = University.objects.create(**data.dict())
    return university

@api.get("/rankings", response=List[RankingSchema])
def list_rankings(request):
    return Ranking.objects.all()
