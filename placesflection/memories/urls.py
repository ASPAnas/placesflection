from django.urls import path
from . import views


urlpatterns = [
    path("", views.list, name="list"),
    path("create", views.create, name="create"),
    path("<int:memory_id>/", views.details, name="details"),
]
