from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Variant
from .serializers import ProductSerializer, VariantSerializer
from .models import Product
import uuid
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
