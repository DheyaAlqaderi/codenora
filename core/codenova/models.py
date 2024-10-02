from django.db import models

# Create your models here.
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)  # Name of the project
    file = models.FileField(upload_to="projects/")  # File associated with the project

    def __str__(self):
        return self.name
