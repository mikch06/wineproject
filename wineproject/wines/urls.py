from django.urls import path
from .views import *

urlpatterns = [
    path("", WineListView.as_view(), name="wine_list"),
    path("<int:pk>/", WineDetailView.as_view(), name="wine_detail"),
    path("<int:pk>/edit/", WineUpdateView.as_view(), name="wine_edit"),
    path("new/", WineCreateView.as_view(), name="wine_new"),
    path("wines/<int:pk>/delete/", wine_delete, name="wine_delete"),
]
