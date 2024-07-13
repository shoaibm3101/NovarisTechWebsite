from django.db import models

# Create your models here.
class Applicant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    position = models.CharField(max_length=200)
    message = models.TextField(default="No Message")

    def __str__(self):
        return f"{self.name}: {self.email}"