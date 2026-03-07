from typing import List, Optional
from ninja import NinjaAPI, Schema, ModelSchema
from ninja.pagination import paginate, PageNumberPagination
from ninja.security import HttpBearer
from django.shortcuts import get_object_or_404
from .models import University, Ranking
from django.http import JsonResponse

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "ninja-token-2024":
            return token

api = NinjaAPI(title="University Ranking API (Django Ninja)", auth=GlobalAuth())

from django.http import JsonResponse, Http404
from ninja.errors import ValidationError

# --- Standard Error Response ---
@api.exception_handler(Http404)
def on_404(request, exc):
    return api.create_response(
        request,
        {"error": True, "message": "Resource not found", "code": 404},
        status=404,
    )

@api.exception_handler(ValidationError)
def on_validation_error(request, exc):
    return api.create_response(
        request,
        {"error": True, "message": "Validation error", "details": exc.errors, "code": 422},
        status=422,
    )

@api.exception_handler(Exception)
def global_exception_handler(request, exc):
    return api.create_response(
        request,
        {"error": True, "message": "An internal server error occurred", "details": str(exc), "code": 500},
        status=500,
    )

# --- Schemas ---
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

# --- Universities Endpoints ---
@api.get("/universities", response=List[UniversitySchema], auth=None)
@paginate(PageNumberPagination, page_size=50)
def list_universities(request):
    """
    Returns a paginated list of universities. 
    Query params: ?page=1
    """
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

# --- Rankings Endpoints ---
@api.get("/rankings", response=List[RankingSchema], auth=None)
@paginate(PageNumberPagination, page_size=50)
def list_rankings(request):
    return Ranking.objects.all()

@api.post("/rankings", response={201: RankingSchema})
def create_ranking(request, data: RankingSchema):
    ranking_data = data.dict(exclude={'id'})
    ranking = Ranking.objects.create(**ranking_data)
    return 201, ranking

@api.put("/rankings/{ranking_id}", response=RankingSchema)
def update_ranking(request, ranking_id: int, data: RankingSchema):
    ranking = get_object_or_404(Ranking, id=ranking_id)
    for attr, value in data.dict(exclude_unset=True, exclude={'id'}).items():
        setattr(ranking, attr, value)
    ranking.save()
    return ranking

@api.delete("/rankings/{ranking_id}", response={204: None})
def delete_ranking(request, ranking_id: int):
    ranking = get_object_or_404(Ranking, id=ranking_id)
    ranking.delete()
    return 204, None
