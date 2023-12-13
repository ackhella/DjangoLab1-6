from ..models import Article
from rest_framework import viewsets
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ItemSerializer


def list(self, request):
    queryset = self.get_queryset()
    serializer = ItemSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
