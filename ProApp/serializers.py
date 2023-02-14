from rest_framework import serializers
from .models import Project, ProjectImage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'data_classes', 'dataset_type']


class ProjectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectImage
        fields = '__all__'
