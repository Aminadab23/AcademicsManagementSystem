from django.db import models

# Create your models here.
class Academy(models.Model):
    Ac_name = models.CharField(max_length=100 )
    description = models.TextField()
    logo = models.ImageField(upload_to='ACM/Academies', default='default.jpg')
    official_web= models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.Ac_name
class ICTDescription(models.Model):
    name= models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self)->str:
        return 'ICT Academy Description'
    