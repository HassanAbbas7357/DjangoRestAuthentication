from django.urls import path
from .views import *


urlpatterns = [
    path('', ProjectListApiView.as_view(), name='project-list-api'),
    path('<int:pk>/detail', ProjectRetrieveUpdateDestroyApiView.as_view(), name='project-retrieve-update-delete-api'),
    path('images', ProjectImageListApiView.as_view(), name='project-image-list-api'),
    path('images/create', ProjectImageCreateApiView, name='image'),
    path('images/<int:pk>/', ProjectImageRetrieveUpdateDestroyApiView.as_view(),
         name='project-image-retrieve-update-delete-api')
]
