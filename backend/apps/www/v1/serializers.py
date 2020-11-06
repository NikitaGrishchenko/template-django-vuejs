from rest_framework import serializers
from ..models import Www


class WwwSerializer(serializers.ModelSerializer):
    """ Список задач """

    # category = CategoryListSerializer()
    # category = serializers.CharField(source="category.name")

    class Meta:
        model = Www
        fields = "__all__"
