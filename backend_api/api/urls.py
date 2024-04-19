from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path

router = DefaultRouter()

router.register(r'reports', GeneralReportsAV, basename='task-file')

urlpatterns = [
    # Include the router's generated URLs
    path('', include(router.urls)),
]
