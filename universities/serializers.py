from rest_framework import serializers
from .models import University, Ranking

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    rankings = RankingSerializer(many=True, read_only=True)
    
    class Meta:
        model = University
        fields = ['id', 'name', 'country', 'city', 'website', 'founded_year', 'rankings']
