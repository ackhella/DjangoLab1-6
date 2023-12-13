from ..models import Article
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Article

        fields = ('id', 'name', 'author', 'date_created', 'description', 'cover')