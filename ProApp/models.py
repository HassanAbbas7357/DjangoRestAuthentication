from django.db import models
from authentication.models import User


# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255, verbose_name='Project Name')
    data_classes = models.CharField(max_length=255, verbose_name='Data Classes')
    dataset_type = models.CharField(max_length=255, verbose_name='Dataset Type')

    def __str__(self):
        return f'{str(self.user)} --- {str(self.project_name)}'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return str(self.project)
