from django.db import connection
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from backend_api.models import *
from rest_framework import viewsets, status


class GeneralReportsAV(viewsets.ModelViewSet):
    queryset = GeneralReport.objects.none()

    def get_queryset(self):
        return GeneralReport.objects.all()
