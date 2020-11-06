from django.urls import path

from .views import WwwListView, WwwDetailView

app_name = "www"

urlpatterns = [
    path("", WwwListView.as_view(), name="index"),
    path("<int:pk>/", WwwDetailView.as_view()),
]
