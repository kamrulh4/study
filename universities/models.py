from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField(max_length=255, blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name

class Ranking(models.Model):
    university = models.ForeignKey(University, related_name='rankings', on_delete=models.CASCADE)
    year = models.IntegerField()
    world_rank = models.IntegerField()
    total_score = models.FloatField(blank=True, null=True)
    
    class Meta:
        unique_together = ('university', 'year')
        ordering = ['world_rank']

    def __str__(self):
        return f"{self.university.name} - {self.year} (Rank: {self.world_rank})"
