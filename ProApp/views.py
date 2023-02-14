from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Project, ProjectImage
from .serializers import ProjectSerializer, ProjectImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from django.shortcuts import get_object_or_404

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


# Create your views here.

class ProjectListApiView(ListCreateAPIView):
    projects = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        projects = Project.objects.filter(user=self.request.user)
        return projects


class ProjectRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'pk'


class ProjectImageListApiView(ListAPIView):
    projectImage = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        projects = Project.objects.filter(user=self.request.user)
        pros = [i.id for i in projects]
        projectImage = ProjectImage.objects.filter(project__in=projects)
        return projectImage


class ProjectImageRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'



@api_view(['POST'])
def ProjectImageCreateApiView(request):
    # try to send 1000  images in batch from react.js so that server can easily handle all images without getting errors
    lst = []
    for i in request.FILES.getlist('image'):
        lst.append({'image': i, 'project': request.data['project']})

    serializer = ProjectImageSerializer(data=lst, many=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"data": "Dataset Uploaded", 'status': status.HTTP_200_OK})
