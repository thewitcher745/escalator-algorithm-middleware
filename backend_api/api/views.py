from django.db import connection
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from backend_api.api.serializers import *
from backend_api.models import *
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination


class GeneralReportsAV(viewsets.ModelViewSet):
    queryset = GeneralReport.objects.all()
    serializer_class = ReportsSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        return serializer.data
