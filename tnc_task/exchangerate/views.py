from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_api_key.models import APIKey
from rest_framework_simplejwt.authentication import JWTAuthentication
from .utils import get_exchange_rate
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer, APIKeySerializer


class CreateListExchangeRateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ExchangeRateSerializer
    queryset = ExchangeRate.objects.all()

    def initialize_request(self, request, *args, **kwargs):
        self.action = self.action_map.get(request.method.lower())
        return super().initialize_request(request, *args, **kwargs)

    def get_authenticators(self):
        if self.action == 'create':
            return [JWTAuthentication()]
        return []

    def get_permissions(self):
        if self.action == 'list':
            return [HasAPIKey()]
        else:
            return [IsAuthenticated(), HasAPIKey()]
            
    def get_queryset(self):
        valid_limits = [10, 30]
        queryset = self.queryset
        limit = int(self.request.query_params.get('limit', '0'))
        if limit and limit in valid_limits:
            queryset = queryset[:limit]
        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        exchange_rate = get_exchange_rate()
        print(exchange_rate)
        serializer = self.serializer_class(data=exchange_rate)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class CreateAPIKeyView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = APIKeySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            api_key, key = APIKey.objects.create_key(name=data['key_name'])
            return Response({'api_key': key}, status=status.HTTP_200_OK)
