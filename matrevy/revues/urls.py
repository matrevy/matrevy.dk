from django.urls import path

from .views import RevueListView, RevueDetailView


app_name = "revues"

urlpatterns = [
    path("", RevueListView.as_view(), name="index"),
    path("<slug:slug>", RevueDetailView.as_view(), name="detail"),
]
