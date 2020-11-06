from rest_framework import generics
from ..models import Www
from .serializers import WwwSerializer
from rest_framework.permissions import AllowAny


class WwwListView(generics.ListCreateAPIView):
    """ Вывод списка задач """

    permission_classes = [AllowAny]
    serializer_class = WwwSerializer
    queryset = Www.objects.all()


class WwwDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Обновление, удаление, детальная информация задачи """

    permission_classes = [AllowAny]
    serializer_class = WwwSerializer
    queryset = Www.objects.all()
