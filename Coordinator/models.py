from django.db import models

from AcademicManager.models import Academy

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length= 100)
    academy = models.ForeignKey(Academy, on_delete=models.CASCADE, related_name="NewCourse")
    payment= models.DecimalField(decimal_places=2, max_digits=6)
    duriation = models.IntegerField()

    def __str__(self):
        return self.title