from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status
from .models import *
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brend']
    ordering_fields = ['narx']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ism','tel']
    ordering_fields = ['qarz']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class BuyurtmaModelViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class AdminModelViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class HaydovchiModelViewSet(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
