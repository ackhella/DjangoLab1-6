from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, JsonResponse

from .api.serializers import ItemSerializer
from .models import Article
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
# Create your views here.


def index(request):
    data = Article.objects.order_by('-date_created')
    if request.method == 'GET':
        serializer = ItemSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
