from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")