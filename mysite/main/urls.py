from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("special/<int:num>", views.special, name="special")
]
