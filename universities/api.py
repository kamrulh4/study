from typing import List, Optional
from ninja import NinjaAPI, Schema, ModelSchema
from ninja.security import HttpBearer
from django.shortcuts import get_object_or_404
from .models import University, Ranking

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "ninja-token-2024":  # For demonstration; in production, use a real DB token
            return token

api = NinjaAPI(title="University Ranking API (Django Ninja)", auth=GlobalAuth())

class RankingSchema(ModelSchema):
    class Meta:
        model = Ranking
        fields = ['id', 'year', 'world_rank', 'total_score']

class UniversitySchema(ModelSchema):
    rankings: List[RankingSchema] = []
    
    class Meta:
        model = University
        fields = ['id', 'name', 'country', 'city', 'website', 'founded_year']

class UniversityCreateSchema(Schema):
    name: str
    country: str
    city: str
    website: str = None
    founded_year: int = None

class UniversityUpdateSchema(Schema):
    name: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    website: Optional[str] = None
    founded_year: Optional[int] = None

@api.get("/universities", response=List[UniversitySchema], auth=None)
def list_universities(request):
    return University.objects.all().prefetch_related('rankings')

@api.get("/universities/{university_id}", response=UniversitySchema, auth=None)
def get_university(request, university_id: int):
    return get_object_or_404(University, id=university_id)

@api.post("/universities", response={201: UniversitySchema})
def create_university(request, data: UniversityCreateSchema):
    university = University.objects.create(**data.dict())
    return 201, university

@api.put("/universities/{university_id}", response=UniversitySchema)
def update_university(request, university_id: int, data: UniversityUpdateSchema):
    university = get_object_or_404(University, id=university_id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(university, attr, value)
    university.save()
    return university

@api.delete("/universities/{university_id}", response={204: None})
def delete_university(request, university_id: int):
    university = get_object_or_404(University, id=university_id)
    university.delete()
    return 204, None

@api.get("/rankings", response=List[RankingSchema], auth=None)
def list_rankings(request):
    return Ranking.objects.all()
