import time

from django.db import connection
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from backend_api.api.serializers import *
from backend_api.models import *
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination


class DynamicPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_page_size(self, request):
        page_size = request.query_params.get(self.page_size_query_param, self.page_size)
        try:
            page_size = int(page_size)
        except ValueError:
            page_size = self.page_size
        return page_size


class GeneralReportsAV(viewsets.ModelViewSet):
    queryset = GeneralReport.objects.all()
    serializer_class = ReportsSerializer
    pagination_class = DynamicPagination

    def get_queryset(self):
        delay = self.request.query_params.get('delay')
        paginated_queryset = self.paginate_queryset(self.queryset)
        serializer = self.serializer_class(paginated_queryset, many=True)
        if delay:
            time.sleep(int(delay))
        return serializer.data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        return self.get_paginated_response(queryset)
